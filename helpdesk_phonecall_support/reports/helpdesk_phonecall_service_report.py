# -*- coding: utf-8 -*-

from odoo import api, fields, models


class HelpdeskPhonecallReport(models.Model):
    _name = 'helpdesk.phonecall.report'

partner_and_user = fields.Float(compute='_compute_report',
                                store=True)


@api.multi
@api.depends('partner_id')
def _compute_report(self):
    self.teste_ex = 1.0 if self.state == 'open' else 0.0
    self.teste_ex2 = 1.0 if self.state == 'done' else 0.0
