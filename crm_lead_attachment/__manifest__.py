# -*- coding: utf-8 -*-

{
    'name': 'CRM Lead Attachment',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'This module insert attachments in crm lead',
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
    ],
    'installable': False,
}
