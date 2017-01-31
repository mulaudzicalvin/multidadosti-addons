# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

import tempfile
import os

import odoo
from odoo import api, fields, models, report

from ..tools.misc import mount_path_jasper
from ..jasper import jasper_report


class Report(report.interface.report_int):

    def __init__(self, name, model, parser=None):
        # Remove report name from list of services if it already
        # exists to avoid report_int's assert. We want to keep the
        # automatic registration at login, but at the same time we
        # need modules to be able to use a parser for certain reports.
        if name in odoo.report.interface.report_int._reports:
            del odoo.report.interface.report_int._reports[name]

        super(Report, self).__init__(name)
        self.model = model
        self.parser = parser

    def create(self, cr, uid, ids, datas, context=None):

        datas['env'] = api.Environment(cr, uid, context or {})

        rep_xml_set = datas['env']['ir.actions.report.xml'].search(
            [('report_name', '=', self.name[7:]),
             ('report_type', 'ilike', 'jasper_report')])

        obj_report_xml = rep_xml_set[0]

        db_parameters = {
            'username': obj_report_xml.db_obj.user_field,
            'database': obj_report_xml.db_obj.db_name,
            'host': obj_report_xml.db_obj.host,
            'port': obj_report_xml.db_obj.port,
            'password': obj_report_xml.db_obj.password,
            'driver': obj_report_xml.db_obj.connector,
        }

        # SQL tuple, ie. (id, id2, id3), of odoo records id to use in WHERE
        # statement.
        rec_ids = '(%s)' % ','.join(map(str, ids))

        template_dir = mount_path_jasper(datas['env'].cr.dbname,
                                         obj_report_xml._table,
                                         obj_report_xml.id)

        path = os.path.join(template_dir, obj_report_xml.template_filename)

        parameters = {
            'ODOO_RECORD_IDS': rec_ids,
        }

        # Add ODOO_REPORT_PATH parameter only exist subreports
        if obj_report_xml.sub_report_ids:
            parameters['ODOO_REPORT_PATH'] = template_dir

        jasper = jasper_report.JasperReport()
        data = jasper.process(path,
                              obj_report_xml.jasper_output_format,
                              parameters=parameters,
                              db_parameters=db_parameters)

        return data.decode('base64'), obj_report_xml.jasper_output_format


class IrActionReportXml(models.Model):

    _inherit = 'ir.actions.report.xml'

    report_type = fields.Selection(
        selection_add=[('jasper_report', 'Jasper Report')])

    jasper_output_format = fields.Selection([('html', 'HTML'),
                                             ('csv', 'CSV'),
                                             ('xls', 'XLS'),
                                             ('rtf', 'RTF'),
                                             ('odt', 'ODT'),
                                             ('ods', 'ODS'),
                                             ('pdf', 'PDF')],
                                            string='Output Format',
                                            default='pdf')

    db_obj = fields.Many2one('jasper.report.db.source',
                             string='Database')

    template = fields.Binary(string='Report Template', help='The root template'
                                                            ' of report.')
    template_filename = fields.Char()

    sub_report_ids = fields.One2many('ir.actions.jasper.sub.report',
                                     'action_report_xml_id',
                                     string='SubReports',
                                     help='Subreport .jrxml templates. '
                                          'This templates are compile in '
                                          '.jasper file.')

    @api.multi
    def write(self, values):
        res = super(IrActionReportXml, self).write(values)

        if self.report_type == 'jasper_report':

            # Compile jasper sub reports
            self._compile_sub_report()

            # Copy .jrxml of template to 'filestore' Odoo folder
            self._build_root_report()

        return res

    @api.multi
    def _build_root_report(self):

        template_dir = mount_path_jasper(self.env.cr.dbname, self._table,
                                         self.id)
        template_dir = os.path.join(template_dir, self.template_filename)

        with open(template_dir, 'w') as f:
            f.write(self.template.decode('base64'))

    @api.multi
    def _compile_sub_report(self):
        jasper = jasper_report.JasperReport()
        template_dir = mount_path_jasper(self.env.cr.dbname, self._table,
                                         self.id)

        # Create temporary .jrxml files to compile them to .jasper
        # We need the make this to generate report, because jasper use
        # .jasper file of subreport to generate final report
        for sub_report in self.sub_report_ids:
            with tempfile.NamedTemporaryFile(suffix='.jrxml') as file_temp:
                file_temp.write(sub_report.template.decode('base64'))
                file_temp.flush()

                output = sub_report.template_filename.replace('.jrxml', '')
                output = os.path.join(template_dir, output)
                jasper.compile(file_temp.name, output_file=output)

    def _lookup_report(self, name):
        """
        Look up a report definition.
        """
        # First lookup in the deprecated place, because if the report
        # definition has not been updated, it is more likely
        # the correct definition is there.
        # Only reports with custom parser specified in Python are still there.
        query = "SELECT * FROM ir_act_report_xml WHERE \
        report_type='jasper_report' and report_name=%s limit 1"
        self.env.cr.execute(query, (name,))
        record = self.env.cr.dictfetchone()

        if not record:
            return super(IrActionReportXml, self)._lookup_report(name)

        # Calling Jasper
        return IrActionReportXml.register_jasper_report(name, record['model'])

    @staticmethod
    def register_jasper_report(report_name, model_name):
        name = 'report.%s' % report_name

        # Register only if it didn't exist another "jasper_report"
        # with the same name given that developers might prefer/need
        # to register the reports themselves.
        # For example, if they need their own parser.
        if name in odoo.report.interface.report_int._reports:
            if isinstance(odoo.report.interface.report_int._reports[name],
                          IrActionReportXml):
                return odoo.report.interface.report_int._reports[name]

            del odoo.report.interface.report_int._reports[name]

        return Report(name, model_name)


class IrActionReportJasperSubReport(models.Model):
    _name = 'ir.actions.jasper.sub.report'
    _rec_name = 'template_filename'
    _description = 'Jasper SubReports'

    template = fields.Binary(string='Template', required=True,
                             help='.jrxml file of template.')
    template_filename = fields.Char()
    action_report_xml_id = fields.Many2one('ir.actions.report.xml')
