from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError


class TestCalendarEventPartner(TransactionCase):

    def setUp(self):
        super(TestCalendarEventPartner, self).setUp()
        self.calendar_event_1 = self.env.ref('calendar.calendar_event_1')

        self.wizard = self.env['calendar.event.finish'].create(
            {'calendar_event_id': self.calendar_event_1.id})

    def test_action_finish_calendar_event_raise_exception(self):

        self.calendar_event_1.event_state = 'done'

        with self.assertRaises(UserError):
            self.wizard.action_finish_calendar_event()

        self.calendar_event_1.event_state = 'cancel'

        with self.assertRaises(UserError):
            self.wizard.action_finish_calendar_event()

    def test_action_finish_calendar_event_ok(self):
        self.calendar_event_1.event_state = 'open'

        ret = self.wizard.action_finish_calendar_event()

        self.assertIsInstance(ret, dict)
        self.assertEqual(ret['type'], 'ir.actions.act_window_close')

        self.assertEqual(self.calendar_event_1.event_state, 'done')
