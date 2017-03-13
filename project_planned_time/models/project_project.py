# -*- coding: utf-8 -*-

from odoo import models, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    planned_time = fields.Float(string='Planned Time')
