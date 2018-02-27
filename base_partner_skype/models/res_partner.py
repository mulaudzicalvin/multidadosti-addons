from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    skype = fields.Char(string='Skype')
