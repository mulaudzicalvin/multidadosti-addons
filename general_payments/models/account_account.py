# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountAccount(models.Model):

    _inherit = 'account.account'

    code_first_digit = fields.Char(compute='_compute_code_first_digit',
                                   string='Code First Digit',
                                   store=True)

    @api.multi
    @api.depends('code')
    def _compute_code_first_digit(self):
        for rec in self:
            rec.code_first_digit = rec.code[0] if rec.code else ''
