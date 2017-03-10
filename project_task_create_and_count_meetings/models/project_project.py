# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProjectProject(models.Model):

    _inherit = 'project.project'

    event_number = fields.Integer(compute='_compute_event_number',
                                    string='Number of Meetings')

    @api.multi
    def _compute_event_number(self):
        for record in self:
            cal_events = record.calendar_event_ids.filtered(
                lambda r: r.event_state == 'open')
            record.event_number = len(cal_events)
