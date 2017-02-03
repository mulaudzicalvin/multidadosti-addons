# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class CRMStage(models.Model):
    _inherit = "crm.stage"

    allow_quotation = fields.Boolean(string='Allow Quotation',
                                     default=True,
                                     help='Allow create quotation when '
                                          'opportunity is in this state.')


class CRMLead(models.Model):
    _inherit = "crm.lead"

    send_quotation = fields.Boolean(related="stage_id.allow_quotation",
                                    readonly="True", invisible="1")
