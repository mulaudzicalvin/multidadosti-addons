# -*- coding: utf-8 -*-
import datetime

from odoo.exceptions import UserError

from odoo.addons.helpdesk_phonecall_support.tests.\
    test_helpdesk_phonecall_confirm import TestHelpDeskPhoneCallConfirm


class TestHelpDeskPhoneCallConfirmTimesheet(TestHelpDeskPhoneCallConfirm):

    def setUp(self):
        super(TestHelpDeskPhoneCallConfirmTimesheet, self).setUp()

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

        timesheet = self.env['account.analytic.line'].search(
            [('helpdesk_id', '=', phonecall.id)])

        self.assertEqual(phonecall.description, timesheet.name)
        self.assertEqual(phonecall.user_id.id, timesheet.user_id.id)
        self.assertEqual(phonecall.partner_id.id, timesheet.partner_id.id)
        self.assertEqual(phonecall.project_id.id, timesheet.project_id.id)
        self.assertEqual(phonecall.company_id.id, timesheet.company_id.id)
        self.assertEqual(phonecall.start_date_hour[:10], timesheet.date)

        # Calculamos o tempo de duracao e verificamos se o tempo correto
        # esta sendo armazenado
        fmt = '%Y-%m-%d %H:%M:%S'
        d1 = datetime.datetime.strptime(phonecall.start_date_hour, fmt)
        d2 = datetime.datetime.strptime(phonecall.finish_date_hour, fmt)

        # Convert total seconds in hours in decimal format
        # When load the float field in screen, the widget
        # 'float_time' will go show time in to HH:MM format
        hours_diff_decimal = (d2 - d1).total_seconds() / 3600.0

        self.assertEqual(timesheet.unit_amount, hours_diff_decimal)
