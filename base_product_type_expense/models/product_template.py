# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    type = fields.Selection(selection_add=[('expense', 'Expense')])

    @api.onchange('type')
    def _onchange_type(self):
        if self.type == 'expense':
            self.sale_ok = False
            self.purchase_ok = False
