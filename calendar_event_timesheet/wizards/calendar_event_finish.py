# -*- coding: utf-8 -*-

import datetime

from odoo import api, models


class CalendarEventFinish(models.TransientModel):
    _inherit = 'calendar.event.finish'

    @api.multi
    def finish_calendar_event(self):
        self.ensure_one()
        res = super(CalendarEventFinish, self).finish_calendar_event()

        ce = self.calendar_event_id

        if ce.project_id and ce.event_state == 'done':
            dt = datetime.datetime.strptime(ce.start_datetime,
                                            '%Y-%m-%d %H:%M:%S')

            partners = [item.id for item in ce.partner_ids
                        if item.parent_id == ce.company_partner_id]

            users = \
                self.env['res.users'].search([('partner_id', 'in', partners)])

            # Create Timesheet to any user in users list
            for user in users:
                values = self._get_account_analytic_line_values(
                    user=user, calendar_event=ce, start_datetime=dt)

                self.env['account.analytic.line'].create(values)

        return res

    @api.multi
    def _get_account_analytic_line_values(self, user, calendar_event,
                                          start_datetime):
        self.ensure_one()
        values = {
            'name': calendar_event.event_feedback,
            'date': start_datetime.date(),
            'user_id': user.id,
            'project_id': calendar_event.project_id.id,
            'unit_amount': calendar_event.event_duration,
            'calendar_event_id': calendar_event.id,
        }

        if calendar_event.task_id:
            values['task_id'] = calendar_event.task_id.id
            values['project_task_type_id'] = calendar_event.task_id.stage_id.id

        return values
