from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _


class CalendarEventFinish(models.TransientModel):
    _name = 'calendar.event.finish'
    _description = 'Wizard to finish calendar event'

    calendar_event_id = fields.Many2one(comodel_name='calendar.event',
                                        string='Calendar Event')

    @api.multi
    def finish_calendar_event(self):
        self.ensure_one()

        if self.calendar_event_id.event_state != 'open':
            raise UserError(_("To finish this event, it must be in 'Open' "
                              "state!"))
        else:
            self.calendar_event_id.event_state = 'done'
            return {'type': 'ir.actions.act_window_close'}
