from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError


class TestBaseConfirmDialog(TransactionCase):

    def setUp(self):
        super(TestBaseConfirmDialog, self).setUp()
        self.confirm_dialog = self.env['base.confirm.wizard'].create({
            'message': 'Test Message',
            'method': 'toggle_activ'
        })

    def test_confirm_base_confirm_dialog(self):
        partner_id = self.env.ref('base.res_partner_4').id
        with self.assertRaises(AccessError):
            self.confirm_dialog.with_context({
                'active_ids': [partner_id],
                'active_model': 'res.partner',
            }).yes()

        self.confirm_dialog.method = 'toggle_active'
        self.confirm_dialog.with_context({
            'active_ids': [partner_id],
            'active_model': 'res.partner',
        }).yes()

        self.assertEqual(self.env['res.partner'].search(
            [('id', '=', partner_id)]).ids, [])
