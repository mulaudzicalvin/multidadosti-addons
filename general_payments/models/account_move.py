# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    title_status = fields.Char(string=u"Status do Título",
                               compute='_compute_title_status')

    @api.multi
    @api.depends('user_type_id', 'date_maturity')
    def _compute_title_status(self):
        for aml in self:
            if aml.user_type_id.type == 'receivable' and aml.reconciled:
                aml.title_status = 'received'
            elif aml.user_type_id.type == 'payable' and aml.reconciled:
                aml.title_status = 'payed'
            elif (not aml.reconciled and aml.date_maturity <
                    fields.Datetime.now()):
                aml.title_status = 'to_expire'
            elif (not aml.reconciled and aml.date_maturity >=
                    fields.Datetime.now()):
                aml.title_status = 'expired'
            else:
                aml.title_status = 'unknown'
