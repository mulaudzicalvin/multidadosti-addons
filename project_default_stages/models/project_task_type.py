# -*- coding: utf-8 -*-

from odoo import fields, models


class ProjectTaskType(models.Model):

    _inherit = 'project.task.type'

    is_default = fields.Boolean(string='Default',
                                default=True,
                                help='Allows assignment of the current stage '
                                     'to new projects that will be created.')

    _sql_constraints = [('project_task_type_name_uniq', 'unique (name)',
                         'Already stage with same name!')]
