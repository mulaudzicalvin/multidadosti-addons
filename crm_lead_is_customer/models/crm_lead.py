# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Lead(models.Model):
    _inherit = 'crm.lead'

    negotiation = fields.Text(string='Negotiation')

    sale_originator = fields.Many2one('res.users', string='Sale Originator')

    attachment_number = fields.Integer(compute='_compute_attachment_number',
                                       string='Number of Attachments')

    partner_id = fields.Many2one('res.partner', string='Customer',
                                 track_visibility='onchange', index=True,
                                 required=True)

    @api.multi
    def action_set_won(self):
        rec = super(Lead, self).action_set_won()
        self.partner_id.customer = True
        self.next_activity_id = False
        return rec

    @api.multi
    def action_set_lost(self):
        ret = super(Lead, self).action_set_lost()
        self.next_activity_id = False
        return ret

    @api.multi
    def _compute_attachment_number(self):
        attachment_data = self.env['ir.attachment'].read_group(
            [('res_model', '=', 'crm.lead'),
             ('res_id', 'in', self.ids)], ['res_id'], ['res_id'])

        attachment = dict(
            (data['res_id'], data['res_id_count']) for data in attachment_data)

        for expense in self:
            expense.attachment_number = attachment.get(expense.id, 0)

    @api.multi
    def action_get_attachment_tree_view(self):
        attachment_action = self.env.ref('base.action_attachment')
        action = attachment_action.read()[0]

        action['context'] = {
            'default_res_model': self._name,
            'default_res_id': self.ids[0],
        }
        action['domain'] = str([('res_model', '=', self._name),
                                ('res_id', 'in', self.ids)])

        search_view = self.env.ref(
            'crm_lead_is_customer.ir_attachment_view_search_crm_lead')

        action['search_view_id'] = [search_view.id]
        return action
