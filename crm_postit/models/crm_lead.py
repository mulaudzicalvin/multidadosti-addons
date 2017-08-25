# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    postit_ids = fields.Many2many(comodel_name='prisme.postit',
                                  relation='crm_lead_prisme_postit_rel',
                                  string='Postit')

    postit_count = fields.Integer(string='Postit',
                                  default=0,
                                  compute='_compute_postit_count')

    @api.depends('postit_ids')
    def _compute_postit_count(self):
        for rec in self:
            rec.postit_count = len(rec.postit_ids)

    @api.multi
    def action_redirect_postit(self):
        """ Redireciona para a tela de postit"""

        action = self.env['ir.actions.act_window'].for_xml_id(
            'prisme_postit', 'action_prisme_postit')

        view_id = self.env.ref('prisme_postit.view_prisme_postit_form')
        action['domain'] = [('id', 'in', self.postit_ids.ids)]
        action['view_id'] = view_id.id
        action['view_ids'] = [view_id.id]
        action['view_mode'] = 'form'
        action['view_type'] = 'form'
        action['context'] = {
            'default_lead_ids': self.ids,
            'default_partner_id': self.partner_id.id,
        }

        return action
