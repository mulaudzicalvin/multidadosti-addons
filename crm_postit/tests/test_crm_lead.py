# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase


class TestCrmLead(TransactionCase):

    def setUp(self):
        super(TestCrmLead, self).setUp()

        values = {
            'name': 'Teste',
            'description': 'Teste',
            'assigned_to': [(6, 0, self.env.ref('base.user_demo').ids)],
        }

        self.crm_lead = self.env.ref('crm.crm_case_24')
        self.post_it = self.env['prisme.postit'].create(values)

    def test__compute_postit_count(self):
        initial_amount = self.crm_lead.postit_count
        self.crm_lead._compute_postit_count()
        self.assertEqual(self.crm_lead.postit_count, initial_amount)

        self.crm_lead.postit_ids = [(6, 0, self.post_it.ids)]
        self.crm_lead._compute_postit_count()
        self.assertEqual(self.crm_lead.postit_count, initial_amount + 1)

    def test_action_redirect_postit(self):
        self.crm_lead.postit_ids = [(6, 0, self.post_it.ids)]

        action = self.crm_lead.action_redirect_postit()

        self.assertListEqual(action['domain'],
                             [('id', 'in', self.post_it.ids)])

        self.assertIn('default_lead_ids', action['context'])
        self.assertIn('default_partner_id', action['context'])

        self.assertEqual(action['context']['default_lead_ids'],
                         self.crm_lead.ids)
        self.assertEqual(action['context']['default_partner_id'],
                         self.crm_lead.partner_id.id)

        view_id = self.env.ref('prisme_postit.view_prisme_postit_form').id
        self.assertEqual(action['view_id'], view_id)

        self.assertEqual(action['view_ids'], [view_id])
        self.assertEqual(action['view_mode'], 'form')
        self.assertEqual(action['view_type'], 'form')
