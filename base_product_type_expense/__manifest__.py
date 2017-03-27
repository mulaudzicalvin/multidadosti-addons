# -*- coding: utf-8 -*-

{
    'name': 'Base Product Type Expense',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'Expense registration to use in contracts.',
    'category': 'Base',
    'contributors': [
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
    ],
    'depends': [
        'product',
        'br_account',
    ],
    'data': [
        'views/product_template.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}
