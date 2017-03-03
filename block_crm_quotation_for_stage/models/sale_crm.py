# -*- coding: utf-8 -*-

from odoo import fields, models


class CRMStage(models.Model):
    _inherit = "crm.stage"

    allow_quotation = fields.Boolean(default=True,
                                     help='Allow create quotation when '
                                          'opportunity is in this state.')


class CRMLead(models.Model):
    _inherit = "crm.lead"

    send_quotation = fields.Boolean(related="stage_id.allow_quotation",
                                    readonly="True", invisible="1")
