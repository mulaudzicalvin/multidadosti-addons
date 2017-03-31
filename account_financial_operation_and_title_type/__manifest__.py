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
     Type in account.move.line model, and reformats the account.move.line
     view""",
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
    ],
    'depends': [
        'br_account_payment',
        'br_boleto',
    ],
    'data': [
        'data/account_financial_operation.xml',
        'data/account_title_type.xml',
        'security/ir.model.access.csv',
        'views/account_financial_operation.xml',
        'views/account_move_line.xml',
        'views/account_title_type.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
