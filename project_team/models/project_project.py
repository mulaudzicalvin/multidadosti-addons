from odoo import fields, models


class ProjectProject(models.Model):

    _inherit = 'project.project'

    project_team_id = fields.Many2one(comodel_name='project.team',
                                      string='Project Team')

    team_member_ids = fields.Many2many(comodel_name='res.users',
                                       string='Project Team Members',
                                       readonly=True,
                                       related='project_team_id.member_ids')
