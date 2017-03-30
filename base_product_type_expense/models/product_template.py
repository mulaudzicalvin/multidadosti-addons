# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    type = fields.Selection(selection_add=[('expense', 'Expense')])
    # debit_ok = fields.Boolean(string='Can be debited',
    #                           help='Specify whether the product can be '
    #                                'debited in an HR expense.')

    @api.onchange('type')
    def _onchange_type(self):
        if self.type == 'expense':
            self.can_be_expensed = True
            self.sale_ok = False
            self.purchase_ok = False
