# -*- coding: utf-8 -*-

{
    'name': 'Account Replace Purchase Menu',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Tools',
    'summary': """Account Replace Purchase Menu.""",
    'contributors': [
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
    ],
    'depends': [
        'purchase',

    ],
    'data': [
        'views/account_replace_invoice_menu.xml',
        'views/purchase_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
