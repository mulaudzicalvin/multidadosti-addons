# -*- coding: utf-8 -*-

from odoo import models, fields


class CalendarEvent(models.Model):

    _inherit = "calendar.event"

    project_id = fields.Many2one("project.project",
                                 string="Projetos")

    task_id = fields.Many2one("project.task", string="Tarefas")
