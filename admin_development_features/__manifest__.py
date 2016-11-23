# -*- coding: utf-8 -*-
#    Admin Development Features to Odoo
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Michell Stuttgart <m.faria@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Admin Development Features',
    'version': '8.0.1.0.0',
    'description': 'Checks the technical features box for admin user, set '
               'user like sale manager',
    'summary': 'Prepare Odoo to development. Not use this module in '
               'production environment',
    'category': 'Administration',
    'author': 'MultidadosTI',
    'website': 'https://github.com/multidadosti-erp/multidadosti-addons',
    'license': 'AGPL-3',
    'depends': [
        'admin_technical_features',
    ],
    'data': [
        'views/res_groups.xml',
    ],
    'installable': False,
    'auto_install': False,
}
