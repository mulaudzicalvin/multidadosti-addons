# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    planned_time = fields.Float(string='Planned Time')

    progress = fields.Float(compute='_compute_progress',
                            string='Hours: Planned x Performed in the Task',
                            group_operator="avg")

    @api.depends('planned_time')
    def _compute_progress(self):
        records = self.env['account.analytic.line'].search([
            ('project_id', '=', self.id)])

        total_horas = 0
        for record in records:
            total_horas += record.unit_amount

        if self.planned_time > 0 and total_horas > 0:
            self.progress = 100 * (total_horas / self.planned_time)
        else:
            self.progress = 0
