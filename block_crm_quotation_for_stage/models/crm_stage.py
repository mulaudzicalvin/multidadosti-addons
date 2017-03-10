# -*- coding: utf-8 -*-

from odoo import fields, models


class CrmStage(models.Model):
    _inherit = "crm.stage"

    allow_quotation = fields.Boolean(string='Allow Quotation',
                                     default=True,
                                     help='Allow create quotation when '
                                          'opportunity is in this state.')
