# -*- coding: utf-8 -*-
#    Remove boolean upgrade
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Aldo Soares <a.soares@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Remove boolean upgrade',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'https://github.com/multidadosti-erp/multidadosti-addons',
    'summary': 'Refactory/Customize',
    'description': """

This module refactor these base modules:
========================================

* mass_mailing (Mass Mailing Campaigns)
* stock (Inventory Management)
* base_setup (Initial Setup Tools)
* sale (Sales)
* account (Invoicing)
* website_sale (eCommerce)
* project (Project)
* point_of_sale (Point of Sale)
* crm (CRM)

Remove all fields with widget *boolean_upgrade*.
                       """,
    'category': 'Web',
    'sequence': 99,
    'depends': [
        'mass_mailing',
        'stock',
        'base_setup',
        'sale',
        'account',
        'website_sale',
        'project',
        'point_of_sale',
        'crm',

    ],
    'data': [
        'views/view_remove_boolean_upgrade.xml',
    ],
    'installable': True,
}
