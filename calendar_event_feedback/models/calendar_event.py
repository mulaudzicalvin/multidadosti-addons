# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    event_feedback = fields.Text(string='Event Feedback',
                                 copy=False,
                                 readonly=True)
    event_duration = fields.Float(string='Event Duration',
                                  copy=False,
                                  readonly=True)

    @api.multi
    def action_finish_calendar_event(self):
        self.ensure_one()
        res = super(CalendarEvent, self).action_finish_calendar_event()

        res['context']['default_event_feedback'] = self.event_feedback
        res['context']['default_event_duration'] = self.event_duration

        return res
