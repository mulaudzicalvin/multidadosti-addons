# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProject(models.Model):

    _inherit = 'project.project'

    calendar_event_ids = fields.One2many(comodel_name="calendar.event",
                                         inverse_name="project_id",
                                         string=u"Eventos de Calendário")
