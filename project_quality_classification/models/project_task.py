from odoo import fields, models

PRIORITY_CLASSIFICATION = [
    ('0', 'Muito Baixa'),
    ('1', 'Baixa'),
    ('2', 'Média'),
    ('3', 'Alta'),
    ('4', 'Muito Alta'),
]


class ProjectTask(models.Model):
    _inherit = 'project.task'

    priority = fields.Selection(selection=PRIORITY_CLASSIFICATION)
