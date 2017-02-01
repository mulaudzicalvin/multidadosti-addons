# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import fields, models


class LineToInvoice(models.Model):

    _name = 'line.to.invoice'

    name = fields.Char(string='Name', required=True)
    factor = fields.Float(string='Discount (%)', required=True)
