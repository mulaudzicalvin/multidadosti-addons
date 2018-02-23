from odoo import fields, models


class AccountAnalyticLineToInvoice(models.Model):

    _name = 'account.analytic.line.to.invoice'

    name = fields.Char(string='Name', required=True)
    factor = fields.Float(string='Discount (%)', required=True)
    billable = fields.Boolean(string='Billable', default=True)
