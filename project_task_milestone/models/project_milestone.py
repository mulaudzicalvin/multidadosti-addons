# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProjectMilestone(models.Model):
    _name = 'project.milestone'

    STATE = {'open': [('readonly', False)]}

    name = fields.Char(string='Name',
                       required=True,
                       readonly=True,
                       states=STATE)

    description = fields.Text(string='Description',
                              readonly=True,
                              states=STATE)

    due_date = fields.Date(string='Due Date',
                           readonly=True,
                           states=STATE)

    task_count = fields.Integer(string='Tasks Count',
                                compute='_compute_task_count',
                                readonly=True,
                                default=0)

    project_task_ids = fields.Many2many(comodel_name='project.task',
                                        readonly=True,
                                        string='Project Task',
                                        states=STATE)

    state = fields.Selection(string='State',
                             selection=[('open', 'Open'),
                                        ('closed', 'Closed')],
                             default='open',
                             required=True)

    @api.multi
    @api.depends('project_task_ids')
    def _compute_task_count(self):
        """ Calcula a quantidade de tarefas relacionadas a milestone.
        """
        for milestone in self:
            milestone.task_count = len(milestone.project_task_ids.ids)

    @api.multi
    def action_close_milestone(self):
        """ Fecha a milestone. Utilizado quando a campanha é encerrada."""
        for milestone in self:
            milestone.state = 'closed'

    @api.multi
    def action_reopen_milestone(self):
        """Reabre a milestone"""
        for milestone in self:
            milestone.state = 'open'
