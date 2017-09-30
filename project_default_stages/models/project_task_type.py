# -*- coding: utf-8 -*-

from odoo import models, fields


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    sequence = fields.Integer('sequence',
                              help="Sequence for the handle task stages.",
                              default=1)
