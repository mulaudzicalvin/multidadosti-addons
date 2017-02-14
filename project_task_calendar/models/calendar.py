# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    project_id = fields.Many2one('project.project', string='Projeto')
    task_id = fields.Many2one('project.task', string='Tarefa')
    partner_id = fields.Many2one('res.partner', string='Cliente')
    meeting_state = fields.Selection([
        ('open', 'Open'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ], string='State', default='open')
    time = fields.Float(string="Time")

