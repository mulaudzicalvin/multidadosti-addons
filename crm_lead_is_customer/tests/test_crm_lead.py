# -*- coding: utf-8 -*-

from odoo.tests import TransactionCase


class TestLead(TransactionCase):

    def test_action_set_won(self):

        lead = self.env.ref('crm.crm_case_11')
        lead.partner_id.customer = False

        self.assertFalse(lead.partner_id.customer)

        # testando metodo para deixar o campo costumer verdadeiro
        ret = lead.action_set_won()

        # verificando se o campo partner esta preenchido
        self.assertTrue(lead.partner_id.customer)

        # Verificando o retorno do metodo
        self.assertTrue(ret)
        self.assertIsInstance(ret, bool)
