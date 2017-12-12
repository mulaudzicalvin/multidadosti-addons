# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProjectMilestone(models.Model):
    _inherit = 'project.milestone'

    STATE = {'open': [('readonly', False)]}

    issue_count = fields.Integer(string='Issues Count',
                                 compute='_compute_issue_count',
                                 readonly=True,
                                 default=0)

    project_issue_ids = fields.Many2many(comodel_name='project.issue',
                                         readonly=True,
                                         string='Project Issue',
                                         states=STATE)

    @api.multi
    @api.depends('project_issue_ids')
    def _compute_issue_count(self):
        """ Calcula a quantidade de incidentes relacionadas a milestone.
        """
        for milestone in self:
            milestone.issue_count = len(milestone.project_issue_ids.ids)
