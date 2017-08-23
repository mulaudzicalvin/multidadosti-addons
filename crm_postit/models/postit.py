# -*- coding: utf-8 -*-
from __future__ import print_function
from odoo import api, fields, models


class PrismePostIt(models.Model):
    """ Post It data """
    _inherit = 'prisme.postit'

    opportunity_count = fields.Integer(string='Opportunity',
                                       compute='_compute_opportunity_count')

    lead_ids = fields.Many2many(comodel_name='crm.lead', string='Leads')

    @api.multi
    def _compute_opportunity_count(self):
        for rec in self:
            rec.opportunity_count = len(self.lead_ids)

    @api.multi
    def action_redirect_crm_lead(self):
        action = self.env['ir.actions.act_window'].for_xml_id(
            'crm', 'crm_lead_opportunities')

        action['domain'] = [('postit_ids', '=', self.id)]
        action['context'] = {
            'default_postit_ids': self.ids,
            'default_partner_id': self.partner_id.id,
        }
        return action
