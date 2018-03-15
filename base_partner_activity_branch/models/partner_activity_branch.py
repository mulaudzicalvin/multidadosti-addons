from odoo import fields, models


class PartnerActivityBranch(models.Model):
    _name = 'partner.activity.branch'

    name = fields.Char(string='Activity Branch')
    description = fields.Text(string='Description')
