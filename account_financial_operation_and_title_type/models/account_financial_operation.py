# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountFinancialOperation(models.Model):

    _name = 'account.financial.operation'

    description = fields.Char(string='Description')

    active = fields.Boolean(string='Active', default=True)
