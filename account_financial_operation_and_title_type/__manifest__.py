# -*- coding: utf-8 -*-

{
    'name': 'Account - New fields: Financial Operation and Title Type',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Account',
    'summary': """This Module adds new fields: Financial Operations and Title
     Type in account.move.line model""",
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
    ],
    'depends': [
        'br_account_payment',
    ],
    'data': [
        'data/account_financial_operation.xml',
        'data/account_title_type.xml',
        'views/account_move_line.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
