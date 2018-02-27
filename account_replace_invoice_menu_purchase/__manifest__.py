{
    'name': 'Account Replace Invoice Menu in Purchase',
    'version': '11.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Tools',
    'summary': """Account Replace Invoice Menu in Purchase.""",
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
    ],
    'depends': [
        'purchase',
        'account_replace_invoice_menu',
    ],
    'data': [
        'views/purchase_order.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
