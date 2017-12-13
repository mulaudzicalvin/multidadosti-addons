# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestAccountPayment(TransactionCase):
    def setUp(self):
        super(TestAccountPayment, self).setUp()
        inv_partner = self.env.ref('base.res_partner_2')
        company = self.env.ref('base.main_company')
        journal = self.env['account.journal'].create(
            {'name': 'Journal - Test', 'code': 'STPJ',
             'type': 'purchase', 'company_id': company.id})
        
        destination_journal = self.env['account.journal'].create(
            {'name': 'Destination Journal - Test', 'code': 'DTJO',
             'type': 'purchase', 'company_id': company.id})

        self.payment_1 = self.env['account.payment'].create({
            'payment_type': 'outbound',
            'partner_id': inv_partner.id,
            'payment_method_id': self.env.ref('account.account_payment_method_manual_out').id,
            'partner_type': 'supplier',
            'journal_id': journal.id,
            'destination_journal_id': destination_journal.id,
            'payment_date': '2018-02-22',
            'state': 'reconciled',
            'amount': 500.00,
            'name': 'Payment Test',
        })

    def test__check_destination_journal_id(self):
        with self.assertRaises(ValidationError):
            self.payment_1.destination_journal_id = self.payment_1.journal_id
            self.assertTrue(self.payment_1._check_destination_journal_id())
