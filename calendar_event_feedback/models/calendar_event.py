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
    def action_call_finish_calendar_wizard(self):
        """Finish calendar event from wizard

        Returns:
            [dict] -- ir.actions.act_window dict
        """
        self.ensure_one()

        res = super(CalendarEvent, self).action_call_finish_calendar_wizard()

        res['context']['default_event_feedback'] = self.event_feedback
        res['context']['default_event_duration'] = self.event_duration

        return res
