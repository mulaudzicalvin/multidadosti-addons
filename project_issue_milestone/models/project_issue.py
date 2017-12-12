# -*- coding: utf-8 -*-

from odoo import fields, models


class ProjectIssue(models.Model):

    _inherit = 'project.issue'

    project_milestone_ids = fields.Many2many(comodel_name='project.milestone',
                                             string='Project Milestone')
