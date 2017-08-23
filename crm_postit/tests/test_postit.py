# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase


class TestPostIt(TransactionCase):

    def setUp(self):
        super(TestPostIt, self).setUp()

        values = {
            'name': 'Teste',
            'description': 'Teste',
            'assigned_to': [(6, 0, self.env.ref('base.user_demo').ids)],
        }

        self.post_it = self.env['prisme.postit'].create(values)

    def test__compute_opportunity_count(self):
        self.assertEqual(self.post_it.opportunity_count, 0)
        self.post_it.lead_ids = [(6, 0, self.env.ref('crm.crm_case_19').ids)]
        self.post_it._compute_opportunity_count()
        self.assertEqual(self.post_it.opportunity_count, 1)

    def test_action_redirect_crm_lead(self):
        action = self.post_it.action_redirect_crm_lead()

        self.assertListEqual(action['domain'],
                             [('postit_ids', '=', self.post_it.id)])

        self.assertIn('default_postit_ids', action['context'])
        self.assertIn('default_partner_id', action['context'])

        self.assertEqual(action['context']['default_postit_ids'],
                         self.post_it.ids)
        self.assertEqual(action['context']['default_partner_id'],
                         self.post_it.partner_id.id)
