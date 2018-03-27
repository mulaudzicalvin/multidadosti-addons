from odoo import api, fields, models


class ProjectProject(models.Model):
    _inherit = 'project.project'

    task_origin_feature_count = fields.Integer(compute='_compute_task_origin_count')
    task_origin_issue_count = fields.Integer(compute='_compute_task_origin_count')

    @api.multi
    @api.depends('task_ids', 'task_ids.origin')
    def _compute_task_origin_count(self):

        for project in self:

            features = project.task_ids.filtered(lambda r: r.origin == 'feature')
            project.task_origin_feature_count = len(features)

            issues = project.task_ids.filtered(lambda r: r.origin == 'issue')
            project.task_origin_issue_count = len(issues)
