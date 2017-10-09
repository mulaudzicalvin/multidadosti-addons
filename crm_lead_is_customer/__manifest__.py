# -*- coding: utf-8 -*-

{
    'name': 'CRM Lead - Is Customer',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'This module customizes default value in customer field on '
               'res.partner model',
    'category': 'Web',
    'contributors': [
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
    ],
    'depends': [
        'sales_team',
        'sale_crm',
    ],
    'data': [
        'views/crm_lead.xml',
        'views/sales_team_dashboard.xml',
    ],
    'qweb': [
        "static/src/xml/sales_team_dashboard.xml",
    ],
    'installable': True,
}
