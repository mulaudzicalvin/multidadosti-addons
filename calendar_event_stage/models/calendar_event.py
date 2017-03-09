# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    meeting_state = fields.Selection(string='Meeting State',
                                     selection=[
                                         ('open', 'Open'),
                                         ('done', 'Done'),
                                         ('cancel', 'Cancel'),
                                     ],
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
        if self.meeting_state == 'open':
            self.meeting_state = 'cancel'

    def action_open_calendar_event(self):
        if self.meeting_state == 'cancel':
            self.meeting_state = 'open'

    @api.multi
    def unlink(self):
        for record in self:
            if record.meeting_state in ('done', 'cancel'):
                raise UserError(_('You cannot delete a calendar meeting which'
                                  ' is done or cancelled.'))
        return super(CalendarEvent, self).unlink()
