# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

{
    'name': 'Send and Receive General Payments',
    'summary': """Send and Receive your general payments""",
    'version': '10.0.1.0.0',
    'category': 'Invoicing & Payments',
    'author': 'MultidadosTI',
    'license': 'LGPL-3',
    'website': 'http://www.multidadosti.com.br',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'account_accountant',
        'br_account_payment',
    ],
    'data': [
        'views/account_payment.xml',
    ],
    'installable': True,
    'application': False,
}
