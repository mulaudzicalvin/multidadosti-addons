# -*- coding: utf-8 -*-

from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    PRIORITY_CLASSIFICATION = [
        ('0', 'Lowest'),
        ('1', 'Low'),
        ('2', 'Medium'),
        ('3', 'Hight'),
        ('4', 'Highest'),
    ]

    priority = fields.Selection(selection=PRIORITY_CLASSIFICATION)
