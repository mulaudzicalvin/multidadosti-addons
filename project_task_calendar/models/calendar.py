# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo.exceptions import UserError
from odoo import api, models, fields, _


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    @api.multi
    def get_company_partner(self):
        company_id = \
            self.env['res.company']._company_default_get('calendar.event')

        return company_id.partner_id

    project_id = fields.Many2one('project.project', string='Project')
    task_id = fields.Many2one('project.task', string='Task')
    partner_id = fields.Many2one('res.partner', string='Partner')
    meeting_feedback = fields.Text(string='Meeting Feedback', readonly=True)
    meeting_duration = fields.Float(string='Meeting Duration', readonly=True)
    meeting_state = fields.Selection([('open', 'Open'),
                                      ('done', 'Done'),
                                      ('cancel', 'Cancel')],
                                     string='Meeting State', default='open')
    company_partner_id = fields.Many2one('res.partner',
                                         default=get_company_partner)

    api.multi

    @api.multi
    def unlink(self):
        for record in self:
            if record.meeting_state in ('done', 'cancel'):
                raise UserError(_('You cannot delete a calendar meeting which'
                                  ' is done or cancelled.'))
        return super(CalendarEvent, self).unlink()

    @api.multi
    def done_button(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.calendar.event',
            'view_type': 'form',
            'view_mode': 'form',
            'views': [(False, "form")],
            'target': 'new',
            'context': {
                'default_calendar_event_id': self.id,
                'default_meeting_duration': self.duration,
            }
        }

    def cancel_button(self):
        if self.meeting_state == 'open':
            self.meeting_state = 'cancel'

    def open_button(self):
        if self.meeting_state == 'cancel':
            self.meeting_state = 'open'
