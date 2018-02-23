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

    start_datetime = fields.Datetime(track_visibility='onchange')

    @api.multi
    def action_call_finish_calendar_wizard(self):
        """Call wizard to finish calendar event."""
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

    @api.multi
    def action_cancel_calendar_event(self):
        """Cancel calendar event if state is 'open'.
        """
        for rec in self:
            if rec.event_state == 'open':
                rec.event_state = 'cancel'

    @api.multi
    def action_open_calendar_event(self):
        """Open calendar event if state is 'cancel.
        """
        for rec in self:
            if rec.event_state == 'cancel':
                rec.event_state = 'open'

    @api.multi
    def unlink(self, can_be_deleted=True):
        """Unlink calendar event record.

        Raises:
            UserError -- When calendar event is on 'done' or 'cancel' state.

        Returns:
            boolean -- True if calendar event was deleted, False otherwise.
        """
        for record in self:
            if record.event_state in ('done', 'cancel'):
                raise UserError(_('You cannot delete a calendar event which'
                                  ' is done or cancelled.'))

        return super(CalendarEvent, self).unlink(can_be_deleted=can_be_deleted)
