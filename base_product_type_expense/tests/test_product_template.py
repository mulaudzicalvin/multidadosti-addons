# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase


class TestProductTemplate(TransactionCase):

    def test__onchange_type(self):

        values = {
            'name': 'Produto test',
            'sale_ok': True,
            'purchase_ok': True,
        }

        product = self.env['product.template'].create(values)

        product.type = 'consu'
        product._onchange_type()
        self.assertEqual(product.sale_ok, True)
        self.assertEqual(product.purchase_ok, True)

        product.type = 'expense'
        product._onchange_type()
        self.assertEqual(product.sale_ok, False)
        self.assertEqual(product.purchase_ok, False)
