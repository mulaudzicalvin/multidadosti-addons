# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    planned_time = fields.Float(string='Planned Time')

    progress = fields.Float(compute='_compute_hours_left',
                            string='Hours: Planned x Performed in the Task',
                            group_operator="avg")

    hours_left = fields.Float(compute='_compute_hours_left',
                              string='Hours Left')

    @api.depends('planned_time')
    def _compute_hours_left(self):

        records = self.env['account.analytic.line'].search([
            ('project_id', '=', self.id)]).mapped('unit_amount')

        total_horas = sum(records)

        if self.planned_time > 0 and total_horas > 0:
            self.hours_left = self.planned_time - total_horas
            self.progress = 100 * (total_horas / self.planned_time)
        else:
            self.hours_left = 0
            self.progress = 0
