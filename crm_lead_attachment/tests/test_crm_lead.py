from odoo.tests.common import TransactionCase


class TestCrmLeadAttachment(TransactionCase):
    
    def setUp(self):
        super(TestCrmLeadAttachment, self).setUp()

        # valor no campo datas('YQ==') é a letra 'a' convertida pra base64

        self.crm_lead = self.env.ref('crm.crm_case_26')
        self.attachment = self.env['ir.attachment'].create({
            'res_model': 'crm.lead',
            'res_id': self.crm_lead.id,
            'datas': 'YQ==',
            'name': 'Anexo CRM',
        })

    def test__compute_attachment_number(self):
        self.assertEqual(self.crm_lead.attachment_number, 1)
