# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    locate_partner = fields.Boolean(string='Select Existing Partner?')

    @api.model
    def create(self, vals):
        user = super(ResUsers, self).create(vals)
        user.partner_id.active = user.active
        if user.partner_id.company_id:
            user.partner_id.write({'company_id': user.company_id.id,
                                   'customer': False,
                                   'parent_id': user.company_id.partner_id.id,
                                   'supplier': False})
        return user
