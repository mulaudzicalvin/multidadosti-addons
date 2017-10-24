# -*- coding: utf-8 -*-


{
    'name': 'CRM Replace Menu',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'CRM',
    'summary': 'This module replace CRM to exclusive menu',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
    ],
    'depends': [
        'sale',
        'base_add_partner_filter',
        'web_lead_funnel_chart',
    ],
    'data': [
        'views/res_partner.xml',
        'views/res_config_view.xml',
        'views/crm_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
