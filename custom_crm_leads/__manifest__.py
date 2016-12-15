# -*- coding: utf-8 -*-
#    Custom CRM Leads
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Aldo Soares <soares_aldo@hotmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Custom CRM Leads',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'https://github.com/multidadosti-erp/multidadosti-addons',
    'summary': 'Custom CRM Leads',
    'category': 'Web',
    'sequence': 99,
    'depends': [
        'sale',
        'crm',
        'sale_crm',
    ],
    'data': [
        'views/view_custom_crm_leads.xml',
    ],
    'installable': True,
}
