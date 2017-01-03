# -*- coding: utf-8 -*-

import os
import re
from tempfile import NamedTemporaryFile
import pyjasper
from odoo import models, fields, api


class MultiJasperReport(models.Model):
    _name = 'multi_jasper_report'

    path_report = ""

    name = fields.Char(
        string=u"Nome")

    db_obj = fields.Many2one(
        comodel_name='multi_jasper_dbsource',
        string=u"Base de dados")

    report = fields.Binary(
        string=u"Relatório")

    parameters = fields.Many2many(
        comodel_name="multi_jasper_report_parameters",
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
            input = file_temp.name
            jasper = pyjasper.JasperPy()
            output = jasper.list_parameters(input).execute()
            os.unlink(input)
            param_dic = {}
            param_output = output
            line_param = param_output.split('\n')

            if self.parameters._ids.__len__() > 0:
                self.parameters = [(5)]

            for i in range(len(line_param)):
                param_item = re.findall(r"[\S]+", line_param[i])
                if param_item:
                    param_dic.update({param_item[1]: param_item[2]})
                    self.parameters = [(0, 0, {'name': param_item[1]})]
                    # return output
        else:
            print "Insira um Relatório"

    @api.multi
    def get_report(self):
        self.ensure_one()
        if self.report:
            self.path_report = os.path.dirname(os.path.dirname(__file__)) + '/temp'
            file_temp = NamedTemporaryFile(dir=self.path_report, suffix='.jrxml',
                                           delete=False)
            file_temp.write(self.report.decode('base64'))
            file_temp.close()
            input = file_temp.name
            dict_list = {}
            for item in self.parameters:
                dict_list.update({item.name: item.subquery})

            con_string = self.db_obj.conn_string.split(' ')
            db_param = {}

            for i in range(len(con_string)):
                con_string[i] = con_string[i].split('=')
                db_param.update({con_string[i][0]: con_string[i][1].replace("'", "")})

            db_param["username"] = db_param["user"]
            db_param["database"] = db_param["dbname"]
            db_param["password"] = self.db_obj.password
            db_param["driver"] = self.db_obj.connector
            db_param.pop("user")
            db_param.pop("dbname")

            jasper = pyjasper.JasperPy()
            jasper.process(input, self.path_report, ["pdf"],
                           parameters=dict_list, db_connection=db_param).execute()
            # self.url_report = str(file_temp.name).replace('jrxml', 'pdf')
            # os.unlink(input)
        else:
            print "Insira um Relatório"


class MultiJasperReportParameters(models.Model):
    _name = 'multi_jasper_report_parameters'

    name = fields.Char(
        string=u"Nome")

    subquery = fields.Char(
        string=u"SubQuery")
