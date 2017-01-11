# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# @author Michell Stuttgart <michellstut@gmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

import os
from pyjasper import jasperpy
import tempfile


class JasperReport:

    def __init__(self, username, database, host, port, password, driver):
        self.username = username
        self.database = database
        self.host = host
        self.port = port
        self.password = password
        self.driver = driver

        self.jasper_client = jasperpy.JasperPy()

    def process(self, template, output_format, parameters):

        with tempfile.NamedTemporaryFile(suffix='.jrxml') as file_temp:
            file_temp.write(template.decode('base64'))
            file_temp.flush()

            db_param = {
                'username': self.username,
                'database': self.database,
                'host': self.host,
                'port': self.port,
                'password': self.password,
                'driver': self.driver,
            }

            self.jasper_client.process(file_temp.name,
                                       output_file=tempfile.gettempdir(),
                                       format_list=[output_format],
                                       parameters=parameters,
                                       db_connection=db_param)

            output = file_temp.name.replace('.jrxml', '.%s' % output_format)

            with open(output, 'rb') as file_bin:
                data = file_bin.read().encode('base64')

            os.unlink(output)

        return data

    # def generate_param_dict(self, line_param):
    #     param_dic = {}
    #     for i in range(len(line_param)):
    #         param_item = re.findall(r"[\S]+", line_param[i])
    #         if param_item:
    #             param_dic.update({param_item[1]: param_item[2]})
    #             self.parameters = [(0, 0, {'name': param_item[1]})]
    #     return 0

    # def pass_params(self, file_input):
    #     dict_list = {}
    #     for item in self.parameters:
    #         if item and not item.subquery:
    #             os.unlink(file_input)
    #             raise ValidationError('Empty parameters. Please set any value'
    #                                   ' to them')
    #         dict_list.update({item.name: item.subquery})
    #     return dict_list

    def get_parameters(self, template):

        with tempfile.NamedTemporaryFile(suffix='.jrxml') as file_temp:
            file_temp.write(template.decode('base64'))
            file_temp.flush()

            output = self.jasper_client.list_parameters(file_temp.name)

        return output

    # @api.multi
    # def get_report(self):
    #     self.ensure_one()
    #
    #     report_file = self.create_report_file()
    #
    #     with open(report_file, 'rb') as file_bin:
    #         self.file_report_binary = file_bin.read().encode('base64')
    #         os.unlink(report_file)

    # @api.multi
    # def get_file_report(self):
    #     self.ensure_one()
    #
    #     url = '/web/binary/download_document?' \
    #           'id_rep={0}&' \
    #           'model=jasper.report&' \
    #           'filename={1}_{0}.{2}'.format(self.id, self.name,
    #                                         self.output_format)
    #
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'url': url,
    #         'target': '_blank',
    #     }

# class Binary(http.Controller):
#     @http.route('/web/binary/download_document', type='http', auth="public")
#     @serialize_exception
#     def download_document(self, model, id_rep, filename=None, debug=None):
#
#         file_c = request.env[model].search([("id", "=", id_rep)])
#         file_content = file_c.file_report_binary.decode('base64')
#
#         return request.make_response(file_content, [
#             ('Content-Type', 'application/octet-stream'),
#             ('Content-Disposition', content_disposition(filename))])


# class IrActionReportXML(models.Model):
#     _inherit = 'ir.actions.report.xml'
#
#     jasper_report_id = fields.Many2one('jasper.report')
