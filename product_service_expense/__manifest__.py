# -*- coding: utf-8 -*-

{
    'name': 'Service Expense',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'Group calendar, productivity(post-it) and messages',
    'category': 'Other',
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
    ],
    'depends': [
        'br_account', 'hr_expense'
    ],
    'data': [
        'views/product_service_expense.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
