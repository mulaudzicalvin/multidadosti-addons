# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    event_state = fields.Selection(string='Event State',
                                   track_visibility='onchange',
                                   selection=[
                                       ('open', 'Open'),
                                       ('done', 'Done'),
                                       ('cancel', 'Cancelled'),
                                   ],
                                   copy=False,
                                   default='open')

    @api.multi
    def action_finish_calendar_event(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'calendar.event.finish',
            'view_type': 'form',
            'view_mode': 'form',
            'views': [(False, "form")],
            'target': 'new',
            'context': {
                'default_calendar_event_id': self.id,
            }
        }

    def action_cancel_calendar_event(self):
        if self.event_state == 'open':
            self.event_state = 'cancel'

    def action_open_calendar_event(self):
        if self.event_state == 'cancel':
            self.event_state = 'open'

    @api.multi
    def unlink(self):
        for record in self:
            if record.event_state in ('done', 'cancel'):
                raise UserError(_('You cannot delete a calendar event which'
                                  ' is done or cancelled.'))
        return super(CalendarEvent, self).unlink()

