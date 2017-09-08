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


class ProjectProject(models.Model):
    _inherit = 'project.project'

    quality_classification = fields.Selection(string='Quality',
                                              selection=QUALITY_CLASSIFICATION,
                                              default='0')
