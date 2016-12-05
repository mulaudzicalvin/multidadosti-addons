# -*- coding: utf-8 -*-
#    General Views Customize to Odoo
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Aldo Soares <a.soares@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'General Views Customize to Odoo',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'https://github.com/multidadosti-erp/multidadosti-addons',
    'summary': 'General Views Customize to Odoo',
    'category': 'Web',
    'depends': [
        'web',
        'br_base',
    ],
    'data': [
        'views/general_views_customize.xml',
    ],
    'installable': True,
}
