# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

import odoo
from odoo import api, fields, models, report, release
from jasper_report import JasperReport


class ReportJasper(report.interface.report_int):
    def __init__(self, name, model, parser=None):
        # Remove report name from list of services if it already
        # exists to avoid report_int's assert. We want to keep the
        # automatic registration at login, but at the same time we
        # need modules to be able to use a parser for certain reports.
        if release.major_version == '5.0':
            if name in odoo.report.interface.report_int._reports:
                del odoo.report.interface.report_int._reports[name]
        else:
            if name in odoo.report.interface.report_int._reports:
                del odoo.report.interface.report_int._reports[name]

        super(ReportJasper, self).__init__(name)
        self.model = model
        self.parser = parser

    def create(self, cr, uid, ids, datas, context=None):

        datas['env'] = api.Environment(cr, uid, context or {})

        rep_xml_set = datas['env']['ir.actions.report.xml'].search(
            [('report_name', '=', self.name[7:]),
             ('report_type', 'ilike', 'jasper_report')])

        obj_report_xml = rep_xml_set[0]

        kwargs = {
            'username': obj_report_xml.db_obj.user_field,
            'database': obj_report_xml.db_obj.db_name,
            'host': obj_report_xml.db_obj.host,
            'port': obj_report_xml.db_obj.port,
            'password': obj_report_xml.db_obj.password,
            'driver': obj_report_xml.db_obj.connector,
        }

        jasper = JasperReport(**kwargs)
        data = jasper.process(obj_report_xml.template,
                              obj_report_xml.jasper_output_format,
                              parameters={
                                  'ODOO_RECORD_IDS': '(%s)' % ','.join(
                                      map(str, ids)),
                              })

        return data.decode('base64'), obj_report_xml.jasper_output_format


def register_jasper_report(report_name, model_name):
    name = 'report.%s' % report_name

    # Register only if it didn't exist another "jasper_report"
    # with the same name given that developers might prefer/need
    # to register the reports themselves.
    # For example, if they need their own parser.
    if name in odoo.report.interface.report_int._reports:
        if isinstance(odoo.report.interface.report_int._reports[name],
                      ReportJasper):
            return odoo.report.interface.report_int._reports[name]

        del odoo.report.interface.report_int._reports[name]

    return ReportJasper(name, model_name)


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
                                            string='Jasper Output',
                                            default='pdf')

    db_obj = fields.Many2one('jasper.report.db.source',
                             string='Database', required=True)

    template = fields.Binary(string='Report Template', required=True)
    template_filename = fields.Char(string='Report Template Filename')

    sub_report_ids = fields.One2many('ir.actions.jasper.sub.report',
                                     'action_report_xml_id',
                                     string='SubReports')

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
        return register_jasper_report(name, record['model'])


class IrActionReportJasperSubReport(models.Model):
    _name = 'ir.actions.jasper.sub.report'
    _rec_name = 'template_filename'
    _description = 'Jasper SubReport'

    template = fields.Binary(string='Template', required=True)
    template_filename = fields.Char(string='Sub Report Template Filename')
    action_report_xml_id = fields.Many2one('ir.actions.report.xml')
