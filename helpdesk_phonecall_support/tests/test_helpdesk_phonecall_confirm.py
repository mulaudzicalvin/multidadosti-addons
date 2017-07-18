# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError


class TestHelpDeskPhoneCallConfirm(TransactionCase):

    def setUp(self):
        super(TestHelpDeskPhoneCallConfirm, self).setUp()

        # Cliente do atendimento
        self.partner = self.env.ref('base.res_partner_3')

        # Contato da empresa que iniciou o atendimento
        self.partner_contact = self.env.ref('base.res_partner_address_31')

        # Projeto do cliente
        self.project = self.env.ref('project.project_project_3')

    def test_action_confirm_finish_phonecall(self):

        tag = 'helpdesk_phonecall_support.helpdesk_phonecall_service_tag_01'

        values = {
            'partner_id': self.partner.id,
            'contact_partner_id': self.partner_contact.id,
            'project_id': self.project.id,
            'description': 'Teste',
            'phonecall_tag_id': self.env.ref(tag).id,
        }

        # Finalmente criamos um atendimento
        phonecall = self.env['helpdesk.phonecall.service'].create(values)

        # Referencia para o wizard
        wizard = self.env['helpdesk.phonecall.confirm'].with_context(
            {'active_ids': [phonecall.id]})

        # Executamos o metodo de finalizar o atendimento
        wizard.action_confirm_finish_phonecall()

        self.assertNotEqual(phonecall.finish_date_hour, False)
        self.assertEqual(phonecall.state, 'done')

        # Executamos o metodo de finalizar o atendimento, verificamos
        # se ele obedece o conceito que apenas atendimentos em aberto podem
        # ser finalizados
        self.assertRaises(wizard.action_confirm_finish_phonecall, None,
                          UserError)
