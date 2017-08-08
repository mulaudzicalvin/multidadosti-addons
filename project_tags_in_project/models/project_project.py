# -*- coding: utf-8 -*-

from odoo import models, fields


class ProjectProject(models.Model):

    _inherit = "project.project"

    project_tags_ids = fields.Many2many(comodel_name='project.tags',
                                        string='Tags')

    project_task_type_id = fields.Many2many(
        comodel_name="project.task.type",
        string="Tarefa(s)"
    )
