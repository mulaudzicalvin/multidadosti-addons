# -*- coding: utf-8 -*-

from odoo import fields, models

QUALITY_CLASSIFICATION = [
    ('0', 'Without Classification'),
    ('1', 'Terrible'),
    ('2', 'Bad'),
    ('3', 'Good'),
    ('4', 'Great'),
    ('5', 'Excellent'),
]

PRIORITY_CLASSIFICATION = [
    ('0', 'Very Low'),
    ('1', 'Low'),
    ('2', 'Normal'),
    ('3', 'High')
]


class ProjectProject(models.Model):
    _inherit = 'project.project'

    quality_classification = fields.Selection(string='Situation',
                                              selection=QUALITY_CLASSIFICATION,
                                              default='0')

    priority = fields.Selection(string='Priority',
                                selection=PRIORITY_CLASSIFICATION,
                                default='0')
