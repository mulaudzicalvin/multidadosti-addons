# -*- coding: utf-8 -*-

from odoo import models, fields


class ProjectProject(models.Model):

    _inherit = "project.project"

    attachment_category = fields.Many2one(string='Tags',
                                          comodel_name='attach.category')
