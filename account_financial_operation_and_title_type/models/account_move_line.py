# -*- coding: utf-8 -*-

from odoo import fields, models
import odoo.addons.decimal_precision as dp


class AccountMoveLine(models.Model):

    _inherit = 'account.move.line'

    financial_operation_id = fields.Many2one('account.financial.operation',
                                             string='Financial Operation')

    title_type_id = fields.Many2one('account.title.type',
                                    string='Title Type')

    title_value = fields.Float(string='Minimum Plot Value',
                               digits=dp.get_precision('Product Price'))
