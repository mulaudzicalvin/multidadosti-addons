
from odoo.tests.common import TransactionCase


class TestIrConfigParameters(TransactionCase):

    def setUp(self):
        super(TestIrConfigParameters, self).setUp()

    def test_create_web_base_url_freeze_ir_config_parameter(self):
        # Verifica se o parametro foi criado corretamente
        get_param = self.env['ir.config_parameter'].get_param
        value = get_param('web.base.url.freeze', default=None)
        
        self.assertEqual(value, 'True')
