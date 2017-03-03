# -*- coding: utf-8 -*-

{
    'name': 'Block CRM Quotation for Stage',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'Block CRM Quotation for Stage',
    'category': 'Web',
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'sale_crm',
    ],
    'data': [
        'views/crm_lead.xml',
        'views/crm_stage.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
    ],
    'installable': True,
}
