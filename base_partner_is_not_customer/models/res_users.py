# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, values):
        user = super(ResUsers, self).create(values)
        # user.partner_id.active = user.active
        if not values['partner_id']:
            user.partner_id.write({
                'company_id': user.company_id.id,
                'customer': False,
                'parent_id': user.company_id.partner_id.id,
                'supplier': False,
            })
        return user
