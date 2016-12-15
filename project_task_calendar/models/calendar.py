# -*- coding: utf-8 -*-
# # Project Task Calendar
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <a.soares@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class CalendarEvent(models.Model):

    _inherit = "calendar.event"

    project_id = fields.Many2one("project.project",
                                 string="Projetos")

    task_id = fields.Many2one("project.task", string="Tarefas")
