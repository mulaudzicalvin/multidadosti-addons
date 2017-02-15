# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <m.faria@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import datetime

from odoo import api, fields, models


class WizardCalendarEventDone(models.TransientModel):
    _name = 'wizard.calendar.event'
    _description = 'Wizard to add feedback and real duration time of meeting'

    meeting_feedback = fields.Text(string='Meeting Feedback', required=True)
    meeting_duration = fields.Float(string='Meeting Duration', required=True)
    calendar_event_id = fields.Many2one('calendar.event')

    @api.multi
    def finish(self):
        self.ensure_one()

        ce = self.calendar_event_id
        ce.meeting_state = 'done'
        ce.meeting_feedback = self.meeting_feedback
        ce.meeting_duration = self.meeting_duration

        if ce.project_id and ce.meeting_state == 'done':
            dt = datetime.datetime.strptime(ce.start_datetime,
                                            '%Y-%m-%d %H:%M:%S')

            values = {
                'name': ce.name,
                'date': dt.date(),
                'user_id': ce.user_id.id,
                'project_id': ce.project_id.id,
                'task_id': ce.task_id.id if ce.task_id else False,
                'unit_amount': ce.duration,
            }
            self.env['account.analytic.line'].create(values)
