# -*- coding: utf-8 -*-

from odoo import api, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, values):
        user = super(ResUsers, self).create(values)

        if not values.get('partner_id', False):
            user.partner_id.write({
                'company_id': user.company_id.id,
                'customer': False,
                'parent_id': user.company_id.partner_id.id,
                'supplier': False,
            })

        return user
