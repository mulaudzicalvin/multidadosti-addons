# -*- coding: utf-8 -*-

{
    'name': 'Service Expense',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'Expense registration to use in contracts.',
    'category': 'Other',
    'contributors': [
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
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
