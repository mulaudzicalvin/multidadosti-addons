# -*- coding: utf-8 -*-

from odoo import models


class Lead(models.Model):
    _inherit = 'crm.lead'

    def action_set_won(self):
        rec = super(Lead, self).action_set_won()
        self.partner_id.customer = True
        return rec
