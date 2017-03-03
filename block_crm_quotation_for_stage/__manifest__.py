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
        'views/sale_views.xml',
        'views/view_sale_crm.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
}
