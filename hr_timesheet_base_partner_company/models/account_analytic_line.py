# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    partner_id = fields.Many2one(related='helpdesk_id.partner_id',
                                 string='Partner',)

    helpdesk_id = fields.Many2one(string='helpdesk_id',
                                  comodel_name='helpdesk.phonecall.service',
                                  stored=False)
