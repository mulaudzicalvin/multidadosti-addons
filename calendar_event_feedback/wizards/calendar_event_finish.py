from odoo import api, fields, models


class CalendarEventFinish(models.TransientModel):
    _inherit = 'calendar.event.finish'

    event_feedback = fields.Text(string='Event Feedback')
    event_duration = fields.Float(string='Event Duration')

    @api.multi
    def action_finish_calendar_event(self):
        self.ensure_one()
        res = super(CalendarEventFinish, self).action_finish_calendar_event()
        self.calendar_event_id.event_feedback = self.event_feedback
        self.calendar_event_id.event_duration = self.event_duration
        return res
