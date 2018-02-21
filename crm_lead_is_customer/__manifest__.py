
{
    'name': 'CRM Lead - Is Customer',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '11.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'This module customizes default value in customer field on '
               'res.partner model',
    'category': 'Web',
    'contributors': [
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'sales_team',
        'sale_crm',
    ],
    'data': [
        'views/crm_lead.xml',
    ],
    'installable': True,
}
