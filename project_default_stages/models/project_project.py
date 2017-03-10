# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    bring_default_task_type = fields.Boolean(string='Get default stages',
                                             deafult=True,
                                             help='Add to this project, '
                                                  'all stage defined like '
                                                  'default')

    @api.model
    def create(self, values):
        project = super(ProjectProject, self).create(values)
        if values.get('bring_default_task_type'):

            task_types = self.env['project.task.type'].search([(
                'is_default', '=', 'True')])
            for rec in task_types:
                rec.project_ids = [(4, project.id)]

        return project
