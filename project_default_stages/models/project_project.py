# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    bring_default_task_type = fields.Boolean(string='Get default stages',
                                             default=True,
                                             help='Add to this project, '
                                                  'all stage defined like '
                                                  'default')

    @api.model
    def create(self, values):
        project = super(ProjectProject, self).create(values)
        if not values.get('bring_default_task_type'):
            project.type_ids = [(5,)]
        return project
