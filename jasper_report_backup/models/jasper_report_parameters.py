# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models


class JasperReportParameters(models.Model):
    _name = 'jasper.report.parameters'

    name = fields.Char('Name', required=True)
    subquery = fields.Char('SQL Query')
    report_id = fields.Many2one('jasper.report', string='Report')
