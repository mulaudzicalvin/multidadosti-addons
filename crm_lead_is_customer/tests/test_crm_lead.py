# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase


class TestCrmLeadIsCustomer(TransactionCase):

    def setUp(self):
        super(TestCrmLeadIsCustomer, self).setUp()

        self.crm_lead = self.env.ref('crm.crm_case_26')

    def test_action_set_won(self):
        self.crm_lead.action_set_won()
        self.assertTrue(self.crm_lead.partner_id.customer)
        self.assertFalse(self.crm_lead.next_activity_id)

        self.crm_lead.partner_id = False
        self.crm_lead.action_set_won()
        self.assertFalse(self.crm_lead.partner_id.customer)
        self.assertFalse(self.crm_lead.next_activity_id)

    def test_action_set_lost(self):
        self.crm_lead.action_set_lost()
        self.assertFalse(self.crm_lead.next_activity_id)
