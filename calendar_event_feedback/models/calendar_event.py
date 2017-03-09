# -*- coding: utf-8 -*-

from odoo import fields, models


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    event_feedback = fields.Text(string='Event Feedback', readonly=True)
    event_duration = fields.Float(string='Event Duration', readonly=True)
