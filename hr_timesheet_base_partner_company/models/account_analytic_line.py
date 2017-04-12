# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    helpdesk_id = fields.Many2one(comodel_name='helpdesk.phonecall.service',
                                  string='Helpdesk')
