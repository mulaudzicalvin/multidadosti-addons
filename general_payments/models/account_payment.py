# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html


from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AccountPayment(models.Model):

    _inherit = 'account.payment'

    journal_inout = fields.Many2one(comodel_name='account.account',
                                    string='Account')
    analytic_account_id = fields.Many2one('account.analytic.account',
                                          string='Analytic Account')
    description = fields.Text('Description')

    @api.one
    @api.depends('invoice_ids', 'payment_type', 'partner_type', 'partner_id')
    def _compute_destination_account_id(self):
        super(AccountPayment, self)._compute_destination_account_id()

        if self.journal_inout:
            self.destination_account_id = self.journal_inout.id

    @api.onchange('payment_type')
    def _onchange_payment_type(self):
        res = super(AccountPayment, self)._onchange_payment_type()

        if not self.invoice_ids and not self.payment_type == 'transfer':
            # Set account_account prefix
            if self.payment_type == 'inbound':
                account_prefix = '3'
            elif self.payment_type == 'outbound':
                account_prefix = '4'

            records = self.env['account.account'].search([])
            ids = [rec.id for rec in records if rec.code[0] == account_prefix]
            res['domain']['journal_inout'] = [('id', 'in', ids)]

        return res

    @api.constrains('journal_inout', 'payment_type')
    def _check_journal(self):

        for record in self:

            if record.journal_inout and not self.payment_type == 'transfer':

                if self.payment_type == 'inbound' \
                        and record.journal_inout.code[0] != '3':
                    raise ValidationError(_("Account to 'Receive Money' "
                                            "payment type must starts "
                                            "with '3'!"))

                elif self.payment_type == 'outbound' \
                        and record.journal_inout.code[0] != '4':
                    raise ValidationError(_("Account to 'Send Money' payment "
                                            "type must starts with '4'!"))
