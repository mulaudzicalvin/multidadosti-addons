# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

import os
from pyjasper import jasperpy
import re
import tempfile

from odoo.exceptions import ValidationError
from odoo import http
from odoo.http import request
from odoo.http import content_disposition
from odoo.addons.web.controllers.main import serialize_exception

from odoo import api, fields, models


FORMAT = [('html', 'HTML'),
          ('csv', 'CSV'),
          ('xls', 'XLS'),
          ('rtf', 'RTF'),
          ('odt', 'ODT'),
          ('ods', 'ODS'),
          ('pdf', 'PDF')]


class JasperReport(models.Model):

    _name = 'jasper.report'

    name = fields.Char(string='Name', required=True)
    db_obj = fields.Many2one('jasper.report.db.source', string='Database')

    action_reports = fields.One2many(comodel_name='ir.actions.report.xml',
                                     inverse_name='jasper_report_id',
                                     string='Action Report')

    output_format = fields.Selection(FORMAT, 'Jasper Output', default='pdf')

    template = fields.Binary(string='Report Template')
    template_filename = fields.Char(string='Report Template Filename')

    file_report_binary = fields.Binary('Binary Report File')

    parameters = fields.One2many(comodel_name='jasper.report.parameters',
                                 inverse_name='report_id',
                                 string='Parameters')

    def create_report_file(self):

        with tempfile.NamedTemporaryFile(suffix='.jrxml') as file_temp:

            file_temp.write(self.template.decode('base64'))
            file_temp.flush()

            db_param = {
                "username": self.db_obj.user_field,
                "database": self.db_obj.db_name,
                "host": self.db_obj.host,
                "port": self.db_obj.port,
                "password": self.db_obj.password,
                "driver": self.db_obj.connector
            }

            jasper = jasperpy.JasperPy()
            jasper.process(file_temp.name,
                           output_file=tempfile.gettempdir(),
                           format_list=[self.output_format],
                           parameters=self.pass_params(file_temp.name),
                           db_connection=db_param)

        return file_temp.name.replace(".jrxml", ".%s" % self.output_format)

    def generate_param_dict(self, line_param):
        param_dic = {}
        for i in range(len(line_param)):
            param_item = re.findall(r"[\S]+", line_param[i])
            if param_item:
                param_dic.update({param_item[1]: param_item[2]})
                self.parameters = [(0, 0, {'name': param_item[1]})]
        return 0

    def pass_params(self, file_input):
        dict_list = {}
        for item in self.parameters:
            if item and not item.subquery:
                os.unlink(file_input)
                raise ValidationError('Empty parameters. Please set any value'
                                      ' to them')
            dict_list.update({item.name: item.subquery})
        return dict_list

    @api.multi
    def listing_parameters(self):
        self.ensure_one()

        if self.template:

            with tempfile.NamedTemporaryFile(suffix='.jrxml') as file_temp:

                file_temp.write(self.template.decode('base64'))
                file_temp.flush()
                jasper = jasperpy.JasperPy()
                output = jasper.list_parameters(file_temp.name)

            names = self.parameters.mapped('name')
            rec = [(0, 0, {'name': key}) for key in output if key not in names]

            self.write({
                'parameters': rec,
            })

    @api.onchange('template')
    def change_template(self):
        self.listing_parameters()

    @api.multi
    def get_report(self):
        self.ensure_one()

        report_file = self.create_report_file()

        with open(report_file, 'rb') as file_bin:
            self.file_report_binary = file_bin.read().encode('base64')
            os.unlink(report_file)

    @api.multi
    def get_file_report(self):
        self.ensure_one()

        url = '/web/binary/download_document?' \
              'id_rep={0}&' \
              'model=jasper.report&' \
              'filename={1}_{0}.{2}'.format(self.id, self.name,
                                            self.output_format)

        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': '_blank',
        }


class Binary(http.Controller):
    @http.route('/web/binary/download_document', type='http', auth="public")
    @serialize_exception
    def download_document(self, model, id_rep, filename=None, debug=None):

        file_c = request.env[model].search([("id", "=", id_rep)])
        file_content = file_c.file_report_binary.decode('base64')

        return request.make_response(file_content, [
            ('Content-Type', 'application/octet-stream'),
            ('Content-Disposition', content_disposition(filename))])


# class IrActionReportXML(models.Model):
#     _inherit = 'ir.actions.report.xml'
#
#     jasper_report_id = fields.Many2one('jasper.report')
