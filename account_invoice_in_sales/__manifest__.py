# -*- coding: utf-8 -*-

{
    'name': 'Account Invoice in Sales',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Tools',
    'summary': """Account Invoice in Sales .""",
    'contributors': [
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
    ],
    'depends': [
        'account',
        'sales_team',
        'purchase',
    ],
    'data': [
        'views/account_invoice_in_sales.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
