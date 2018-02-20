# -*- coding: utf-8 -*-

{
    'name': 'Account Detached Payments',
    'summary': """Send and Receive your detached payments""",
    'version': '10.0.1.0.0',
    'category': 'Invoicing & Payments',
    'author': 'MultidadosTI',
    'license': 'LGPL-3',
    'website': 'http://www.multidadosti.com.br',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
    ],
    'depends': [
        'account_accountant',
        'br_account_payment',
    ],
    'data': [
        'templates/assets.xml',
        'views/account_analytic.xml',
        'views/account_move.xml',
        'views/account_payment.xml',
    ],
    'installable': False,
    'auto_install': False,
    'application': False,
}
