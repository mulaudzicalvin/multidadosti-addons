# -*- coding: utf-8 -*-

import os
import re
import pyjasper

from odoo import models, fields, api


class MultiJasperReport(models.Model):
    _name = 'multi_jasper_report'

    path_report = fields.Char()

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



    def listingParameters(self):
        input = os.path.dirname(os.path.abspath(__file__)) + '/exemples/hello_world_params.jrxml'
        jasper = pyjasper.JasperPy()
        output = jasper.list_parameters(input).execute()
        param_dic = {}
        param_output = output
        line_param = param_output.split('\n')
        for i in range(len(line_param)):
            param_item = re.findall(r"[\S]+", line_param[i])
            if param_item:
                param_dic.update({param_item[1]: param_item[2]})

        return output


class MultiJasperReportParameters(models.Model):
    _name = 'multi_jasper_report_parameters'

    name = fields.Char(
        string=u"Nome")

    subquery = fields.Char(
        string=u"SubQuery")
