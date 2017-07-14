# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError


class TestHelpDeskPhoneCallConfirm(TransactionCase):

    def test_action_confirm_finish_phonecall(self):

        # Criamos o cliente
        partner = self.env['res.partner'].create({
            'name': 'Nome Cliente',
            'is_company': True,
            'purchase_warn': 'no - message',
        })

        # Criamos o contato do cliente
        partner_contact = self.env['res.partner'].create({
            'name': 'Nome Contato',
            'is_company': False,
        })

        # Criamos o projeto
        project = self.env['project.project'].create({
            'name': 'Nome Projeto',
            'partner_id': partner.id,
        })

        tag = 'helpdesk_phonecall_support.helpdesk_phonecall_service_tag_01'

        values = {
            'partner_id': partner.id,
            'contact_partner_id': partner_contact.id,
            'project_id': project.id,
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
