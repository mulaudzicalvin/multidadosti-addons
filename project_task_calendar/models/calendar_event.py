# -*- coding: utf-8 -*-

from odoo import api, models, fields


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    project_id = fields.Many2one('project.project', string='Project',
                                 track_visibility='onchange')
    task_id = fields.Many2one('project.task', string='Task',
                              track_visibility='onchange')

    project_name = fields.Char(compute='_compute_record_name')
    task_name = fields.Char(compute='_compute_record_name')

    @api.depends('partner_id', 'project_id', 'task_id')
    def _compute_record_name(self):
        """ Utilizado para exibir nome do projeto e da tarefa na view de
        kanban"""
        super(CalendarEvent, self)._compute_record_name()
        for rec in self:
            rec.project_name = (' * ' + rec.project_id.name
                                if rec.project_id else '')
            rec.task_name = ' * ' + rec.task_id.name if rec.task_id else ''
