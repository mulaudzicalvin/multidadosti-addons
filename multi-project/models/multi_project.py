# -*- coding: utf-8 -*-

from odoo import models, fields


class Meeting(models.Model):
    _inherit = "calendar.event"

    # project_ids = fields.One2many(comodel_name="project.project",
    #                                inverse_name="project_id",
    #                                string="Projetos")

    project_ids = fields.Many2many("project.project",
                                   string="Projetos",
                                   domain=[('partner_id','in', 'attendee_ids')])


    def get_list_partners(self):
        return self.partner_ids
    # task_ids = fields.One2many(comodel_name="project.task",
    #                                inverse_name="task_id",
    #                                string="Tarefas")


# class Project(models.Model):
#     _inherit = "project.project"
#
#     project_id = fields.Many2one(comodel_name="calendar.event",
#                                  string="Projeto")

# class Task(models.Model):
#     _inherit = "project.task"
#
#     task_id = fields.Many2one(comodel_name="calendar.event",
#                                  string="Tarefa")