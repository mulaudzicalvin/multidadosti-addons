
from odoo.tests.common import TransactionCase


class TestIrConfigParameters(TransactionCase):

    def setUp(self):
        super(TestIrConfigParameters, self).setUp()

    def test_create_report_url_ir_config_parameter(self):

        # Verifica se o parametro foi criado corretamente
        get_param = self.env['ir.config_parameter'].get_param
        value = get_param('report.url', default=None)
        
        self.assertEqual(value, 'http://127.0.0.1:8069')
