# -*- coding: utf-8 -*-

from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    partner_ids = fields.Many2many(comodel_name='res.partner',
                                   related='project_id.partner_ids',
                                   string='Related Partners')
