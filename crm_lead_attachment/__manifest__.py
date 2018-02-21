{
    'name': 'CRM Lead Attachment',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '11.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'This module insert attachments in crm lead',
    'category': 'Web',
    'contributors': [
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'crm_lead_is_customer',
    ],
    'data': [
        'views/crm_lead.xml',
    ],
    'installable': True,
}
