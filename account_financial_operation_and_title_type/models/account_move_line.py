# -*- coding: utf-8 -*-

from odoo import fields, models
import odoo.addons.decimal_precision as dp


class AccountMoveLine(models.Model):

    _inherit = 'account.move.line'

    financial_operation = fields.Many2one(
        string='Financial Operation',
        comodel_name='account.financial.operation')

    title_type = fields.Many2one(
        string='Title Type',
        comodel_name='account.title.type')

    title_value = fields.Float(
        string='Minimum Plot Value',
        digits=dp.get_precision('Product Price'))
