# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Lead(models.Model):
    _inherit = 'crm.lead'

    negotiation = fields.Text(string='Negotiation')

    sale_originator = fields.Many2one('res.users', string='Sale Originator')

    @api.multi
    def action_set_won(self):
        rec = super(Lead, self).action_set_won()
        if self.partner_id:
            self.partner_id.customer = True
        self.next_activity_id = False
        return rec

    @api.multi
    def action_set_lost(self):
        ret = super(Lead, self).action_set_lost()
        self.next_activity_id = False
        return ret
