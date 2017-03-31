# -*- coding: utf-8 -*-

from odoo import fields, models


class ProjectProject(models.Model):

    _inherit = 'project.project'

    calendar_event_ids = fields.One2many(comodel_name='calendar.event',
                                         inverse_name='project_id',
                                         readonly=True,
                                         string='Calendar Events')
