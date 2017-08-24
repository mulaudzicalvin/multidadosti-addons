# -*- coding: utf-8 -*-
{
    'name': 'CRM Postit',
    'version': '10.0.1.0.0',
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
        'views/postit_view.xml',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
