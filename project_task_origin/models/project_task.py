# -*- coding: utf-8 -*-

from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    origin = fields.Selection(string='Origin',
                              selection=[('feature', 'Feature'),
                                         ('issue', 'Issue')],
                              required=True,
                              default='feature')
