from odoo import fields, models


class ProjectTask(models.Model):

    _inherit = 'project.task'

    project_milestone_ids = fields.Many2many(comodel_name='project.milestone',
                                             string='Project Milestone')
