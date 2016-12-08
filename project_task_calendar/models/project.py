# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProject(models.Model):

    _inherit = 'project.project'

    calendar_event_ids = fields.One2many(comodel_name="calendar.event",
                                         inverse_name="project_id",
                                         string=u"Eventos de Calendário")

    bring_default_task_type = fields.Boolean(
                                string=u"Trazer estágios padronizados",
                                help=u"Atribui ao atual projeto, todos"
                                     u" os estágios que foram criados "
                                     u"com status Padrão")

    @api.model
    def create(self, vals):
        res = super(ProjectProject, self).create(vals)

        if vals.get('bring_default_task_type'):
            task_types = self.env['project.task.type'].search([(
                'is_default', '=', 'True')])
            for rec in task_types:
                rec.project_ids = [(4, res.id)]

        return res


class MultiProjectTaskType(models.Model):

    _inherit = 'project.task.type'

    is_default = fields.Boolean(string=u"Padrão",
                                help=u"Permite Atribuição do atual estágio"
                                     u" a novos projetos que serão criados")
