# -*- coding: utf-8 -*-

from odoo import fields, models
import odoo.addons.decimal_precision as dp


class AccountTitleType(models.Model):

    _name = 'account.title.type'

    initials = fields.Char(string='Initials', size=3)

    name = fields.Char(string='Name')

    minimum_plot_value = fields.Float(string='Minimum Plot Value',
                                      digits=dp.get_precision('Product Price'))

    allow_cnab_sending = fields.Boolean(string='Allow CNAB Sending')
