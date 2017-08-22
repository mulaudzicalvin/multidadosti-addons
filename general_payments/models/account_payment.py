# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError


class AccountPayment(models.Model):

    _inherit = 'account.payment'

    general_account_id = fields.Many2one(comodel_name='account.account',
                                         string='Account')

    analytic_account_id = fields.Many2one('account.analytic.account',
                                          string='Analytic Account')

    description = fields.Text(string='Description')

    @api.multi
    @api.depends('invoice_ids', 'payment_type', 'partner_type', 'partner_id')
    def _compute_destination_account_id(self):
        self.ensure_one()
        super(AccountPayment, self)._compute_destination_account_id()

        if self.general_account_id:
            self.destination_account_id = self.general_account_id.id

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
            res['domain']['general_account_id'] = [('id', 'in', ids)]

        return res

    def _get_shared_move_line_vals(self, debit, credit, amount_currency,
                                   move_id, invoice_id=False):
        """
            Returns values common to both move lines (except for debit, credit
            and amount_currency which are reversed)
        """
        res = super(AccountPayment, self)._get_shared_move_line_vals(
            debit, credit, amount_currency, move_id, invoice_id=invoice_id)

        if self.invoice_ids:

            for inv in self.invoice_ids:
                self.analytic_account_id = \
                    inv.invoice_line_ids[0].account_analytic_id.id

        # if not self.invoice_ids:
        res['analytic_account_id'] = self.analytic_account_id.id
        return res

    @api.constrains('general_account_id', 'payment_type')
    def _check_general_account(self):

        for record in self:

            if record.general_account_id \
                    and not self.payment_type == 'transfer':

                if self.payment_type == 'inbound' \
                        and record.general_account_id.code[0] != '3':
                    raise ValidationError(_("Account to 'Receive Money' "
                                            "payment type must starts "
                                            "with '3'!"))

                elif self.payment_type == 'outbound' \
                        and record.general_account_id.code[0] != '4':
                    raise ValidationError(_("Account to 'Send Money' payment "
                                            "type must starts with '4'!"))
