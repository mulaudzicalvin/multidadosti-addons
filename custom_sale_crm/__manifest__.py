# -*- coding: utf-8 -*-
#    Custom Sale CRM
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Aldo Soares <soares_aldo@hotmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Custom Sale CRM',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'https://github.com/multidadosti-erp/multidadosti-addons',
    'summary': 'Custom Sale CRM',
    'category': 'Web',
    'sequence': 99,
    'depends': [
        'sale',
        'crm',
        'sale_crm',
    ],
    'data': [
        'views/view_custom_sale_crm.xml',
    ],
    'installable': True,
}
