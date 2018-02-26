from odoo.exceptions import UserError
from odoo.tests.common import TransactionCase


class TestCalendarEventPartner(TransactionCase):

    def setUp(self):
        super(TestCalendarEventPartner, self).setUp()
        self.calendar_event_1 = self.env.ref('calendar.calendar_event_1')
        self.calendar_event_2 = self.env.ref('calendar.calendar_event_2')

        self.calendar_events = self.calendar_event_1
        self.calendar_events |= self.calendar_event_2

        for ce in self.calendar_events:
            ce.event_feedback = 'Feedback'
            ce.event_duration = 3600.0

    def test_action_call_finish_calendar_wizard(self):

        ret = self.calendar_event_1.action_call_finish_calendar_wizard()

        self.assertEqual(ret['context']['default_event_feedback'], 'Feedback')
        self.assertEqual(ret['context']['default_event_duration'], 3600.0)

    def test_action_call_finish_calendar_wizard_raise_exception(self):

        # O metodo deve receber apenas um record, caso contrário o retorno
        # sera comprometido. Aqui, verificamos se o metodo dispara excecao
        # quando o mesmo e invocado com mais de um record
        with self.assertRaises(ValueError):
            self.calendar_events.action_call_finish_calendar_wizard()
