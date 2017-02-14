# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    project_id = fields.Many2one('project.project', string='Projeto')
    task_id = fields.Many2one('project.task', string='Tarefa')
    partner_id = fields.Many2one('res.partner', string='Cliente')
    meeting_state = fields.Selection([
        ('open', 'Open'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ], string='State', default='open')
    meeting_feedback = fields.Text(string='Feedback', readonly=True)
    meeting_duration = fields.Float(string='Duration', readonly=True)

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
            # 'res_id': self.id,
        }

    def cancel_button(self):
        self.meeting_state = 'cancel'

    def open_button(self):
        self.meeting_state = 'open'


class WizardCalendarEventDone(models.TransientModel):
    _name = 'wizard.calendar.event'

    meeting_feedback = fields.Text(string='Feedback', required=True)
    meeting_duration = fields.Float(string='Duration', required=True)
    calendar_event_id = fields.Many2one('calendar.event')

    def finish(self):
        self.calendar_event_id.meeting_state = 'done'
        self.calendar_event_id.meeting_feedback = self.meeting_feedback
        self.calendar_event_id.meeting_duration = self.meeting_duration
