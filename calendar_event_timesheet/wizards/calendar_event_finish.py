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

        if ce.project_id and ce.meeting_state == 'done':
            dt = datetime.datetime.strptime(ce.start_datetime,
                                            '%Y-%m-%d %H:%M:%S')

            partners = [item.id for item in ce.partner_ids
                        if item.parent_id == ce.company_partner_id]

            users = \
                self.env['res.users'].search([('partner_id', 'in', partners)])

            for user in users:

                values = {
                    'name': ce.meeting_feedback,
                    'date': dt.date(),
                    'user_id': user.id,
                    'project_id': ce.project_id.id,
                    'unit_amount': ce.meeting_duration,
                    'calendar_event_id': ce.id,
                }

                if ce.task_id:
                    values['task_id'] = ce.task_id.id
                    values['project_task_type_id'] = ce.task_id.stage_id.id

                self.env['account.analytic.line'].create(values)

        return res
