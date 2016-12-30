# -*- coding: utf-8 -*-

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


class MultiJasperReportParameters(models.Model):
    _name = 'multi_jasper_report_parameters'

    name = fields.Char(
        string=u"Nome")

    subquery = fields.Char(
        string=u"SubQuery")
