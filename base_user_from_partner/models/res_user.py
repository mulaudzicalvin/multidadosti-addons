# -*- coding: utf-8 -*-

from odoo import fields, models, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    locate_partner = fields.Boolean(string='Select Existing Partner?',
                                    help=_("""Allow select a existing
                                           partner to use as base to create
                                           this user."""))
