# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html


from odoo import api, fields, models


class AccountAccount(models.Model):

    _inherit = 'account.account'

    code_first_digit = fields.Char(compute='_get_first_digit', store=True)

    @api.multi
    @api.depends('code')
    def _get_first_digit(self):
        for rec in self:
            rec.code_first_digit = rec.code[0] if rec.code else ''
