{
    'name': 'CRM Postit',
    'version': '11.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Extra Tools',
    'summary': 'This Module link postit with CRM cotation.',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
    ],
    'depends': [
        'crm',
        'prisme_postit',
    ],
    'data': [
        'views/prisme_postit.xml',
        'views/crm_lead.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
