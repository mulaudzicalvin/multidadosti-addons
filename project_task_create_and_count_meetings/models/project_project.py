# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProjectProject(models.Model):

    _inherit = 'project.project'

    meeting_number = fields.Integer(compute='_compute_meeting_number',
                                    string='Number of Meetings')

    @api.multi
    def _compute_meeting_number(self):
        for record in self:
            cal_events = record.calendar_event_ids.filtered(
                lambda r: r.meeting_state == 'open')
            record.meeting_number = len(cal_events)
