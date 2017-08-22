# -*- coding: utf-8 -*-

from odoo import fields
from odoo.exceptions import UserError
from odoo.tests.common import TransactionCase


class TestHelpDeskPhoneCallService(TransactionCase):

    def setUp(self):
        super(TestHelpDeskPhoneCallService, self).setUp()

        # Cliente do atendimento
        partner = self.env.ref('base.res_partner_address_1')

        # Contato da empresa que iniciou o atendimento
        partner_contact = self.env.ref('base.res_partner_address_31')

        # Projeto do cliente
        project = self.env.ref('project.project_project_4')

        tag = 'helpdesk_phonecall_support.helpdesk_phonecall_service_tag_01'
        self.phonecall_tag_id = self.env.ref(tag)

        self.phonecall_values = {
            'partner_id': partner.id,
            'contact_partner_id': partner_contact.id,
            'project_id': project.id,
            'description': 'Teste',
            'phonecall_tag_id': self.phonecall_tag_id.id,
        }

        # Finalmente criamos um atendimento
        self.phonecall = self.env['helpdesk.phonecall.service'].create(
            self.phonecall_values)

    def test__onchange_title(self):

        # Verificamos se o titulo esta vazio
        self.assertFalse(self.phonecall.title)

        now = fields.datetime.now()
        self.phonecall.start_date_hour = now

        title = '%s, %s, %s' % (self.phonecall.start_date_hour,
                                self.phonecall.partner_id.name,
                                self.phonecall.project_id.name)

        # Chamamos o metodo para alteracao do titulo
        self.phonecall._onchange_title()

        # Comparamos os titulos
        self.assertEqual(self.phonecall.title, title)

    def test__onchange_partner_id(self):

        # Alteramos para um usuario que e pessoa fisica
        self.phonecall.partner_id = \
            self.env.ref('base.res_partner_address_1').id

        # Garantimos que o parceiro nao e uma empresa
        self.assertFalse(self.phonecall.partner_id.is_company)

        # Executamos o onchange
        self.phonecall._onchange_partner_id()

        # Verificamos se o parceiro de contato e o parceiro selecionado
        self.assertEqual(self.phonecall.contact_partner_id.id,
                         self.phonecall.partner_id.id)

    def test_action_finish_phonecall(self):

        # Testa se action_finish_phonecall retorna a action corretamente
        self.assertTrue(self.phonecall.phonecall_tag_id)
        self.assertTrue(self.phonecall.description)

        res = self.phonecall.action_finish_phonecall()

        self.assertEqual(res['type'], 'ir.actions.act_window')
        self.assertEqual(res['res_model'], 'helpdesk.phonecall.confirm')
        self.assertEqual(res['view_type'], 'form')
        self.assertEqual(res['view_mode'], 'form')
        self.assertEqual(res['views'], [(False, "form")])
        self.assertEqual(res['target'], 'new')

        # Se phonecall_tag_id ou description forem False, uma excepcao do
        # tipo UserError e lançada
        self.phonecall.phonecall_tag_id = False

        with self.assertRaises(UserError):
            self.phonecall.action_finish_phonecall()

        self.phonecall.phonecall_tag_id = self.phonecall_tag_id.id
        self.phonecall.description = False
        #
        with self.assertRaises(UserError):
            self.phonecall.action_finish_phonecall()

    def test_create(self):

        # Criamos um atendimento com um titulo. Isso e feito para verificar
        # se o metodo create pega a data que esta contida no titulo e atribui
        # para start_date_hour
        self.phonecall_values['title'] = ('2017-08-22 12:49:20, '
                                          'Agrolait, '
                                          'E-Learning Integration')

        phonecall = self.env['helpdesk.phonecall.service'].create(
            self.phonecall_values)

        self.assertEqual(phonecall.start_date_hour, '2017-08-22 12:49:20')
