# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProject(models.Model):

    _inherit = 'project.project'

    calendar_event_ids = fields.One2many(comodel_name="calendar.event",
                                         inverse_name="project_id",
                                         string=u"Eventos de Calendário")


class MultiProjectTaskType(models.Model):

    _inherit = 'project.task.type'

    is_default = fields.Boolean(string=u"Padrão",
                                help=u"Atribui o atual estágio automaticamente"
                                     u" a todos os novos projetos criados")
