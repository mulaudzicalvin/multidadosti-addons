# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase


class TestCalendarEventPartner(TransactionCase):

    def setUp(self):
        super(TestCalendarEventPartner, self).setUp()

        self.ce = self.env.ref('calendar.calendar_event_1')

    def test__compute_record_name(self):
        self.ce.partner_id = self.ce.partner_ids.id
        self.ce._compute_record_name()
        self.assertEqual(self.ce.partner_name, u' * ASUSTeK')

        self.ce.partner_id = False
        self.ce._compute_record_name()
        self.assertEqual(self.ce.partner_name, u'')
