# -*- coding: utf-8 -*-
#    Custom Sale CRM
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Aldo Soares <soares_aldo@hotmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class CustomStage(models.Model):
    _inherit = "crm.stage"

    allow_quotation = fields.Boolean(string=u'Permitir Nova Cotação?',
                                     help=u'Indica se é possivel criar uma '
                                          u'nova cotação neste estágio.')


class CustomLead(models.Model):
    _inherit = "crm.lead"

    send_quotation = fields.Boolean(related="stage_id.allow_quotation",
                                    readonly="True", invisible="1")
