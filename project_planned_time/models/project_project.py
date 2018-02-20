from odoo import api, models, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    planned_time = fields.Float(string='Planned Time',
                                help='Project planned time in hours')

    progress = fields.Float(compute='_compute_hours_left',
                            string='Performed Hours')

    hours_left = fields.Float(compute='_compute_hours_left',
                              string='Hours Left')

    @api.depends('planned_time')
    def _compute_hours_left(self):

        for rec in self:

            records = self.env['account.analytic.line'].search([
                ('project_id', '=', rec.id)]).mapped('unit_amount')

            total_horas = sum(records)

            if rec.planned_time > 0 and total_horas > 0:
                rec.hours_left = rec.planned_time - total_horas
                rec.progress = 100 * (total_horas / rec.planned_time)

            elif rec.planned_time > 0 and total_horas == 0:
                rec.hours_left = rec.planned_time

            else:
                rec.hours_left = 0.0
                rec.progress = 0.0
