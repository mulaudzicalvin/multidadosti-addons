# -*- coding: utf-8 -*-

{
    'name': 'Account Replace Invoice Menu in Sale',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Tools',
    'summary': """Account Replace Invoice Menu in Sale.""",
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
    ],
    'depends': [
        'sales_team',
        'sale',
        'account_replace_invoice_menu',
    ],
    'data': [
        'views/sale.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
