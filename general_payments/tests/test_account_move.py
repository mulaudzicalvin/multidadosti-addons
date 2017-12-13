# -*- coding: utf-8 -*-


from odoo.tests.common import TransactionCase


class TestAccountMoveLine(TransactionCase):
    def setUp(self):
        super(TestAccountMoveLine, self).setUp()
        self.main_company = self.env.ref('base.main_company')
        self.currency_real = self.env.ref('base.BRL')

        self.revenue_account = self.env['account.account'].create({
            'code': '3.0.0',
            'name': 'Receita de Vendas',
            'user_type_id': self.env.ref(
                'account.data_account_type_revenue').id,
            'company_id': self.main_company.id
        })

        self.receivable_account = self.env['account.account'].create({
            'code': '1.0.0',
            'name': 'Conta de Recebiveis',
            'reconcile': True,
            'user_type_id': self.env.ref(
                'account.data_account_type_receivable').id,
            'company_id': self.main_company.id
        })

        self.discount_account = self.env['account.account'].create({
            'code': '4.x.y',
            'name': 'Descontos Concedidos',
            'user_type_id': self.env.ref(
                'account.data_account_type_expenses').id,
            'company_id': self.main_company.id
        })

        self.interest_account = self.env['account.account'].create({
            'code': '3.x.y',
            'name': 'Juros Recebidos',
            'user_type_id': self.env.ref(
                'account.data_account_type_revenue').id,
            'company_id': self.main_company.id
        })

        self.partner_fis = self.env['res.partner'].create({
            'name': 'Nome Parceiro',
            'is_company': False,
            'property_account_receivable_id': self.receivable_account.id,
            'property_account_payable_id': self.receivable_account.id,
        })

        self.journalrec = self.env['account.journal'].create({
            'name': 'Faturas',
            'code': 'INV',
            'type': 'sale',
            'default_debit_account_id': self.revenue_account.id,
            'default_credit_account_id': self.revenue_account.id,
            'update_posted': True,
        })

        self.financial_operation = (
            self.env.ref('br_account.account_financial_operation_6'))

        self.title_type = self.env.ref('br_account.account_title_type_2')

        self.account_move_lines_base_dict = {
            'name': 'Teste Account Move',
            'partner_id': self.partner_fis.id,
            'financial_operation_id': self.financial_operation.id,
            'title_type_id': self.title_type.id,
            'date_maturity': '2017-10-30',
            'quantity': 1,
        }

        # Create account.move.lines dict
        ml1 = {
            'account_id': self.partner_fis.property_account_payable_id.id,
            'credit': 500.0,
        }
        ml1.update(self.account_move_lines_base_dict)

        ml2 = {
            'account_id': self.revenue_account.id,
            'debit': 500.0,
        }
        ml2.update(self.account_move_lines_base_dict)

        # Create account.move dict
        values = {
            'name': 'Teste Move',
            'state': 'posted',
            'ref': '',
            'journal_id': self.journalrec.id,
            'date': '2017-10-30',
            'line_ids': [(0, 0, ml1), (0, 0, ml2)],
        }
        # Create account.move record
        ctx = {
            'journal_type': 'company_expense'
        }

        self.move = self.env['account.move'].sudo().with_context(
            ctx).create(values)

    def test__compute_title_status(self):
        self.move.line_ids[1].reconciled = True
        self.move.line_ids[1]._compute_title_status()
        self.assertEquals(self.move.line_ids[1].title_status, 'received')

        self.move.line_ids[1].user_type_id.type = 'payable'
        self.move.line_ids[1]._compute_title_status()
        self.assertEquals(self.move.line_ids[1].title_status, 'payed')

        self.move.line_ids[1].reconciled = False
        self.move.line_ids[1]._compute_title_status()
        self.assertEquals(self.move.line_ids[1].title_status, 'expired')
