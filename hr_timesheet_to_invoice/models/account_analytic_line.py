# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    account_analytic_line_to_invoice_id = \
        fields.Many2one(comodel_name='account.analytic.line.to.invoice',
                        string='To Invoice')
