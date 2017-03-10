# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    # project_task_type_id = fields.Many2one('project.task.type',
    #                                        string='Project Task State')

    # calendar_event_id = fields.Many2one(comodel_name='calendar.event',
    #                                     readonly=True,
    #                                     string='Calendar Event')

    # to_invoice = fields.Many2one('to.invoice', string='To Invoice')
