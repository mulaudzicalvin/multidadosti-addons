# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    type = fields.Selection(selection_add=[('expense', 'Expense')])
    can_be_expensed = fields.Boolean(string="Can be Expensed",
                                     help="Specify whether the product can be "
                                     "selected in an HR expense.")

    @api.onchange('type')
    def _onchange_type(self):
        if self.type == 'expense':
            self.can_be_expensed = True
            self.sale_ok = False
            self.purchase_ok = False
        else:
            self.can_be_expensed = False
            self.sale_ok = False
            self.purchase_ok = False
