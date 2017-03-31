# -*- coding: utf-8 -*-

from odoo import models, fields
'res.partner'


class PartnerSkype(models.Model):
    _inherit = 'res.partner'

    skype = fields.Char(string='Skype')
