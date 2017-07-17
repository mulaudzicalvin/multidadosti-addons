# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError


class TestHelpDeskPhoneCallConfirm(TransactionCase):

    def setUp(self):
        super(TestHelpDeskPhoneCallConfirm, self).setUp()
        self.main_company = self.env.ref('base.main_company')

        default_partner = {
            'name': 'Nome Parceiro',
            'legal_name': 'Razão Social',
            'zip': '88037-240',
            'street': 'Endereço Rua',
            'number': '42',
            'district': 'Centro',
            'phone': '(48) 9801-6226',
        }

        # Criamos o cliente
        self.partner = self.env['res.partner'].create(dict(
            default_partner.items(),
            cnpj_cpf='05.075.837/0001-13',
            company_type='company',
            is_company=True,
            inscr_est='433.992.727',
            country_id=self.env.ref('base.br').id,
            state_id=self.env.ref('base.state_br_sc').id,
            city_id=self.env.ref('br_base.city_4205407').id,
        ))

        # Criamos o contato do cliente
        self.partner_contact = self.env['res.partner'].create(dict(
            default_partner.items(),
            cnpj_cpf='545.770.154-98',
            company_type='person',
            is_company=False,
            country_id=self.env.ref('base.br').id,
            state_id=self.env.ref('base.state_br_sc').id,
            city_id=self.env.ref('br_base.city_4205407').id
        ))

        # Criamos o projeto
        self.project = self.env['project.project'].create({
            'name': 'Nome Projeto',
            'partner_id': self.partner.id,
        })

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
