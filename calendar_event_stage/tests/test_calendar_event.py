from odoo.exceptions import UserError
from odoo.tests.common import TransactionCase


class TestCalendarEventPartner(TransactionCase):

    def setUp(self):
        super(TestCalendarEventPartner, self).setUp()
        self.calendar_event_1 = self.env.ref('calendar.calendar_event_1')
        self.calendar_event_2 = self.env.ref('calendar.calendar_event_2')

        self.calendar_events = self.calendar_event_1
        self.calendar_events |= self.calendar_event_2

    def test_action_call_finish_calendar_wizard(self):

        ret = self.calendar_event_1.action_call_finish_calendar_wizard()

        self.assertIsInstance(ret, dict)
        self.assertEqual(ret['type'], 'ir.actions.act_window')
        self.assertEqual(ret['res_model'], 'calendar.event.finish')
        self.assertEqual(ret['view_type'], 'form')
        self.assertEqual(ret['view_mode'], 'form')
        self.assertListEqual(ret['views'], [(False, "form")])
        self.assertEqual(ret['target'], 'new')
        self.assertEqual(ret['context']['default_calendar_event_id'],
                         self.calendar_event_1.id)

    def test_action_call_finish_calendar_wizard_raise_exception(self):

        # O metodo deve receber apenas um record, caso contrário o retorno
        # sera comprometido. Aqui, verificamos se o metodo dispara excecao
        # quando o mesmo e invocado com mais de um record
        with self.assertRaises(ValueError):
            self.calendar_events.action_call_finish_calendar_wizard()

    def test_action_cancel_calendar_event_raise_exception(self):
        self.calendar_event_1.event_state = 'done'
        self.calendar_event_2.event_state = 'cancel'

        self.calendar_events.action_cancel_calendar_event()

        self.assertEqual(self.calendar_event_1.event_state, 'done')
        self.assertEqual(self.calendar_event_2.event_state, 'cancel')

    def test_action_cancel_calendar_event_ok(self):
        self.calendar_event_1.event_state = 'open'
        self.calendar_event_2.event_state = 'open'

        self.calendar_events.action_cancel_calendar_event()

        self.assertEqual(self.calendar_event_1.event_state, 'cancel')
        self.assertEqual(self.calendar_event_2.event_state, 'cancel')

    def test_action_open_calendar_event_raise_exception(self):
        self.calendar_event_1.event_state = 'done'
        self.calendar_event_2.event_state = 'open'

        self.calendar_events.action_open_calendar_event()

        self.assertEqual(self.calendar_event_1.event_state, 'done')
        self.assertEqual(self.calendar_event_2.event_state, 'open')

    def test_action_open_calendar_event_ok(self):
        self.calendar_event_1.event_state = 'cancel'
        self.calendar_event_2.event_state = 'cancel'

        self.calendar_events.action_open_calendar_event()

        self.assertEqual(self.calendar_event_1.event_state, 'open')
        self.assertEqual(self.calendar_event_2.event_state, 'open')

    def test_unlink_raise_exception(self):
        self.calendar_event_1.event_state = 'done'
        self.calendar_event_2.event_state = 'open'

        with self.assertRaises(UserError):
            self.calendar_events.unlink()

        self.calendar_event_1.event_state = 'open'
        self.calendar_event_2.event_state = 'cancel'

        with self.assertRaises(UserError):
            self.calendar_events.unlink()

    def test_unlink_ok(self):
        self.calendar_event_1.event_state = 'open'
        self.calendar_event_2.event_state = 'open'
        self.assertTrue(self.calendar_events.unlink())
