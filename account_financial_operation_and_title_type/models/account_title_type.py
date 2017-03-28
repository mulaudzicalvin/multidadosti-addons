# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountTitleType(models.Model):

    _name = 'account.title.type'

    initials = fields.Char(string='Initials', size=3)

    description = fields.Char(string='Description')

    minimum_plot_value = fields.Float(string='Minimum Plot Value')

    allow_cnab_sending = fields.Boolean(string='Allow CNAB Sending')
