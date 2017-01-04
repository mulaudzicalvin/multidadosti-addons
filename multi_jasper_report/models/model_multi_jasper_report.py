# -*- coding: utf-8 -*-

import os
import pyjasper
import re
from tempfile import NamedTemporaryFile

from odoo import http
from odoo.http import request
from odoo.http import content_disposition
from odoo.addons.web.controllers.main import serialize_exception

from odoo import models, fields, api


class MultiJasperReport(models.Model):

    _name = 'multi_jasper_report'

    path_report = ""

    url_param = fields.Char()

    check_parameters = fields.Boolean()

    name = fields.Char(
        string=u"Nome")

    db_obj = fields.Many2one(
        comodel_name='multi_jasper_dbsource',
        string=u"Base de dados")

    report = fields.Binary(
        string=u"Relatório")

    pdf_report = fields.Binary()

    parameters = fields.One2many(
        comodel_name="multi_jasper_report_parameters",
        inverse_name="report_id",
        string=u"Parâmetros")

    @api.multi
    def listing_parameters(self):
        self.ensure_one()
        if self.report:
            file_temp = NamedTemporaryFile(
                dir=os.path.dirname(os.path.dirname(__file__)) + '/temp',
                suffix='.jrxml',
                delete=False)

            file_temp.write(self.report.decode('base64'))
            file_temp.close()
            file_input = file_temp.name
            jasper = pyjasper.JasperPy()
            output = jasper.list_parameters(file_input).execute()
            os.unlink(file_input)
            param_dic = {}
            param_output = output
            line_param = param_output.split('\n')

            for i in range(len(line_param)):
                param_item = re.findall(r"[\S]+", line_param[i])
                if param_item:
                    param_dic.update({param_item[1]: param_item[2]})
                    self.parameters = [(0, 0, {'name': param_item[1]})]

            if len(self.parameters):
                self.check_parameters = True
            else:
                self.check_parameters = False

        return 0

    @api.multi
    def get_report(self):
        self.ensure_one()
        if self.report:
            self.path_report = os.path.dirname(os.path.dirname(__file__)) + \
                               '/temp'

            file_temp = NamedTemporaryFile(dir=self.path_report,
                                           suffix='.jrxml',
                                           delete=False)

            file_temp.write(self.report.decode('base64'))
            file_temp.close()
            file_input = file_temp.name
            dict_list = {}

            for item in self.parameters:
                dict_list.update({item.name: item.subquery})

            db_param = {
                "username": self.db_obj.user_field,
                "database": self.db_obj.dbname,
                "host": self.db_obj.host,
                "port": self.db_obj.port,
                "password": self.db_obj.password,
                "driver": self.db_obj.connector
            }

            jasper = pyjasper.JasperPy()
            jasper.process(file_input,
                           self.path_report,
                           ["pdf"],
                           parameters=dict_list,
                           db_connection=db_param).execute()

            self.url_param = file_temp.name.replace(self.path_report+'/', "")
            self.url_param = self.url_param.replace("jrxml", "pdf")

            try:
                file_pdf = open(os.path.dirname(os.path.dirname(__file__))
                              + '/temp/' + self.url_param, 'rb')
                self.pdf_report = file_pdf.read().encode('base64')
            finally:
                os.unlink(file_temp.name)
                os.unlink(file_temp.name.replace("jrxml", "pdf"))

    @api.multi
    def get_file_report(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/binary/download_document?'
                   'id_rep={0}&'
                   'model={1}&'
                   'filename={2}_{0}.pdf'
                   ''.format(self.id,
                             'multi_jasper_report',
                             self.name),
            'target': 'self',
        }


class Binary(http.Controller):
    @http.route('/web/binary/download_document', type='http', auth="public")
    @serialize_exception
    def download_document(self, model, id_rep, filename=None):

        file_c = request.env[model].search([("id", "=", id_rep)]).pdf_report
        filecontent = file_c.decode('base64')

        return request.make_response(filecontent,
                                     [('Content-Type',
                                       'application/octet-stream'),
                                      ('Content-Disposition'
                                       , content_disposition(filename))])


class MultiJasperReportParameters(models.Model):
    _name = 'multi_jasper_report_parameters'

    report_id = fields.Many2one()

    name = fields.Char(
        string=u"Nome")

    subquery = fields.Char(
        string=u"SubQuery")

