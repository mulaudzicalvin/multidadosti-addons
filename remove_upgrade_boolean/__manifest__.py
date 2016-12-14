# -*- coding: utf-8 -*-
#    Remove upgrade boolean
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Aldo Soares <a.soares@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Remove upgrade boolean',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'https://github.com/multidadosti-erp/multidadosti-addons',
    'summary': 'Refactory/Customize',
    'description': """

This module refactor these base modules:
========================================

* base_setup (Initial Setup Tools)
* sale (Sales)
* account (Invoicing)

Remove all fields with widget *upgrade_boolean*.
                       """,
    'category': 'Web',
    'sequence': 99,
    'depends': [
        'base_setup',
        'sale',
        'account',
    ],
    'data': [
        'views/view_remove_upgrade_boolean.xml',
    ],
    'installable': True,
}
