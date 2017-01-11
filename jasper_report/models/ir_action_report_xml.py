# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

import tempfile
import logging
import os
import time
import odoo
from odoo import api, fields, models, report, release

FORMAT = [('html', 'HTML'),
          ('csv', 'CSV'),
          ('xls', 'XLS'),
          ('rtf', 'RTF'),
          ('odt', 'ODT'),
          ('ods', 'ODS'),
          ('pdf', 'PDF')]


class Report:
    def __init__(self, name, cr, uid, ids, data, context):
        self.name = name
        self.env = data['env']
        self.cr = cr
        self.uid = uid
        self.ids = ids
        self.data = data
        self.model = self.data.get('model', False) or context.get(
            'active_model', False)
        self.context = context or {}
        self.report_path = None
        self.report = None
        self.temporary_files = []
        # self.output_format = data['report_format']

    def execute(self):

        rep_xml_set = self.env['ir.actions.report.xml'].search(
            [('report_name', '=', self.name[7:])])

        jreport = rep_xml_set.jasper_report_id
        jreport.get_report()
        data = jreport.file_report_binary.decode('base64')

        return data, rep_xml_set.jasper_output_format


    # def execute(self):
    #     """
    #     If self.context contains "return_pages = True" it will return
    #     the number of pages of the generated report.
    #     """
    #     logger = logging.getLogger(__name__)
    #
    #     # * Get report path *
    #     # Not only do we search the report by name but also ensure that
    #     # 'report_rml' field has the '.jrxml' postfix. This is needed because
    #     # adding reports using the <report/> tag, doesn't remove the old
    #     # report record if the id already existed (ie. we're trying to
    #     # override the 'purchase.order' report in a new module).
    #     # As the previous record is not removed, we end up with two records
    #     # named 'purchase.order' so we need to destinguish
    #     # between the two by searching '.jrxml' in report_rml.
    #
    #     rep_xml_set = self.env['ir.actions.report.xml'].search(
    #         [('report_name', '=', self.name[7:]),
    #          ('report_rml', 'ilike', '.jrxml')])
    #
    #     data = rep_xml_set[0]
    #
    #     if data['jasper_output']:
    #         self.output_format = data['jasper_output']
    #
    #     self.report_path = data['report_rml']
    #     self.report_path = os.path.join(self.addons_path(), self.report_path)
    #
    #     if not os.path.lexists(self.report_path):
    #         self.report_path = self.addons_path(path=data['report_rml'])
    #
    #     # Get report information from the jrxml file
    #     logger.info("Requested report: '%s'" % self.report_path)
    #     self.report = JasperReport(self.report_path)
    #
    #     # Create temporary input (XML) and output (PDF) files
    #     fd, data_file = tempfile.mkstemp()
    #     os.close(fd)
    #     fd, output_file = tempfile.mkstemp()
    #     os.close(fd)
    #
    #     self.temporary_files.append(data_file)
    #     self.temporary_files.append(output_file)
    #
    #     logger.info("Temporary data file: '%s'" % data_file)
    #     start = time.time()
    #
    #     # If the language used is xpath create the xmlFile in dataFile.
    #     if self.report.language == 'xpath':
    #         if self.data.get('data_source', 'model') == 'records':
    #             generator = CsvRecordDataGenerator(self.report,
    #                                                self.data['records'])
    #         else:
    #             generator = CsvBrowseDataGenerator(self.report, self.model,
    #                                                self.env, self.cr,
    #                                                self.uid, self.ids,
    #                                                self.context)
    #         generator.generate(data_file)
    #         self.temporary_files += generator.temporaryFiles
    #
    #     sub_report_data_files = []
    #
    #     for sub_report_info in self.report.subreports:
    #         sub_report = sub_report_info['report']
    #
    #         if sub_report.language() == 'xpath':
    #             message = 'Creating CSV '
    #
    #             if sub_report_info['pathPrefix']:
    #                 message += 'with prefix %s ' % \
    #                            sub_report_info['pathPrefix']
    #             else:
    #                 message += 'without prefix '
    #
    #             message += 'for file %s' % sub_report_info['filename']
    #             logger.info("%s" % message)
    #
    #             fd, sub_report_data_file = tempfile.mkstemp()
    #             os.close(fd)
    #
    #             sub_report_data_files.append({
    #                 'parameter': sub_report_info['parameter'],
    #                 'dataFile': sub_report_data_file,
    #                 'jrxmlFile': sub_report_info['filename'],
    #             })
    #             self.temporary_files.append(sub_report_data_file)
    #
    #             if sub_report.isHeader():
    #                 generator = CsvBrowseDataGenerator(sub_report,
    #                                                    'res.users', self.env,
    #                                                    self.cr, self.uid,
    #                                                    [self.uid],
    #                                                    self.context)
    #             elif self.data.get('data_source', 'model') == 'records':
    #                 generator = CsvRecordDataGenerator(sub_report,
    #                                                    self.data['records'])
    #             else:
    #                 generator = CsvBrowseDataGenerator(sub_report, self.model,
    #                                                    self.env, self.cr,
    #                                                    self.uid, self.ids,
    #                                                    self.context)
    #             generator.generate(sub_report_data_file)
    #
    #     # Call the external java application that will generate the
    #     # PDF file in outputFile
    #     pages = self.execute_report(data_file, output_file,
    #                                 sub_report_data_files)
    #
    #     elapsed = (time.time() - start) / 60
    #     logger.info("ELAPSED: %f" % elapsed)
    #
    #     # Read data from the generated file and return it
    #     with open(output_file, 'rb') as f:
    #         data = f.read()
    #
    #     # Remove all temporary files created during the report
    #     if tools.config['jasperunlink']:
    #
    #         for f in self.temporary_files:
    #             try:
    #                 os.unlink(f)
    #             except os.error:
    #                 logger.warning("Could not remove file '%s'." % f)
    #
    #     self.temporary_files = []
    #
    #     if self.context.get('return_pages'):
    #         return data, self.output_format, pages
    #     else:
    #         return data, self.output_format

    # def path(self):
    #     return os.path.abspath(os.path.dirname(__file__))
    #
    # def addons_path(self, path=False):
    #     if path:
    #         report_module = path.split(os.path.sep)[0]
    #
    #         # for addons_path in tools.config['addons_path'].split(','):
    #         #     if os.path.lexists(addons_path + os.path.sep + report_module):
    #         #         return os.path.normpath(addons_path + os.path.sep + path)
    #
    #     return os.path.dirname(self.path())
    #
    # def system_user_name(self):
    #     if os.name == 'nt':
    #         import win32api
    #         return win32api.GetUserName()
    #     else:
    #         import pwd
    #         return pwd.getpwuid(os.getuid())[0]
    #
    # def dsn(self):
    #     # host = tools.config['db_host'] or 'localhost'
    #     # port = tools.config['db_port'] or '5432'
    #     # db_name = self.cr.dbname
    #     # return 'jdbc:postgresql://%s:%s/%s' % (host, port, db_name)
    #     pass
    #
    # def user_name(self):
    #     user_name = self.env['ir.config_parameter'].get_param(
    #         'db_user') or self.system_user_name()
    #     return tools.config['db_user'] or user_name
    #
    # def password(self):
    #     password = self.env['ir.config_parameter'].get_param(
    #         'db_password') or ''
    #     return tools.config['db_password'] or password
    #
    # def execute_report(self, data_file, output_file, sub_report_data_files):
    #     locale = self.context.get('lang', 'en_US')
    #
    #     connection_parameters = {
    #         'output': self.output_format,
    #         # 'xml': data_file,
    #         'csv': data_file,
    #         'dsn': self.dsn(),
    #         'user': self.user_name(),
    #         'password': self.password(),
    #         'subreports': sub_report_data_files,
    #     }
    #     parameters = {
    #         'STANDARD_DIR': self.report.standard_directory(),
    #         'REPORT_LOCALE': locale,
    #         'IDS': self.ids,
    #     }
    #     if 'parameters' in self.data:
    #         parameters.update(self.data['parameters'])
    #
    #     server = JasperServer(int(tools.config['jasperport']))
    #     server.setPidFile(tools.config['jasperpid'])
    #     #        java path for jasper server
    #     company_rec = self.env['res.users'].browse(self.uid).company_id
    #     server.javapath = company_rec and company_rec.java_path or ''
    #     server.pidfile = tools.config['jasperpid']
    #     return server.execute(connection_parameters, self.report_path,
    #                           output_file, parameters)


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
        name = self.name

        # if self.parser:
        #     d = self.parser(cr, uid, ids, datas, context)
        #     ids = d.get('ids', ids)
        #     name = d.get('name', self.name)
        #     # Use model defined in ReportJasper definition.
        #     # Necessary for menu entries.
        #     datas['model'] = d.get('model', self.model)
        #     datas['records'] = d.get('records', [])
        #     # data_source can be 'model' or 'records' and lets parser to return
        #     # an empty 'records' parameter while still executing using
        #     # 'records'
        #     datas['data_source'] = d.get('data_source', 'model')
        #     datas['parameters'] = d.get('parameters', {})

        datas['env'] = api.Environment(cr, uid, context or {})
        r = Report(name, cr, uid, ids, datas, context)
        return r.execute()


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

    jasper_report_id = fields.Many2one('jasper.report')

    report_type = fields.Selection(
        selection_add=[('jasper_report', 'Jasper Report')])

    jasper_output_format = fields.Selection(FORMAT,
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
