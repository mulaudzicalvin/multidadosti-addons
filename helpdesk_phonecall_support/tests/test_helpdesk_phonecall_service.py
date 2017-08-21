# -*- coding: utf-8 -*-

from odoo import fields
from odoo.tests.common import TransactionCase


class TestHelpDeskPhoneCallConfirm(TransactionCase):

    def setUp(self):
        super(TestHelpDeskPhoneCallConfirm, self).setUp()

        # Cliente do atendimento
        self.partner = self.env.ref('base.res_partner_3')

        # Contato da empresa que iniciou o atendimento
        self.partner_contact = self.env.ref('base.res_partner_address_31')

        # Projeto do cliente
        self.project = self.env.ref('project.project_project_3')

        tag = 'helpdesk_phonecall_support.helpdesk_phonecall_service_tag_01'

        self.phonecall_values = {
            'partner_id': self.partner.id,
            'contact_partner_id': self.partner_contact.id,
            'project_id': self.project.id,
            'description': 'Teste',
            'phonecall_tag_id': self.env.ref(tag).id,
        }

        # Finalmente criamos um atendimento
        self.phonecall = self.env['helpdesk.phonecall.service'].create(
            self.phonecall_values)

    def test__onchange_title(self):

        self.assertFalse(self.phonecall.title)

        now = fields.datetime.now()
        self.phonecall.start_date_hour = now

        title = '%s, %s, %s' % (self.phonecall.start_date_hour,
                                self.phonecall.partner_id.name,
                                self.phonecall.project_id.name)

        self.phonecall._onchange_title()

        self.assertEqual(self.phonecall.title, title)
