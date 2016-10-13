# -*- coding: utf-8 -*-
#    Disable Powered By Odoo Footer to Odoo
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Michell Stuttgart <m.faria@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': "Disable Powered by Odoo Footer",
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '8.0.1.0.0',
    'website': 'https://github.com/multidadosti-erp/multidadosti-addons',
    'category': 'Web',
    'depends': [
        'web',
    ],
    'data': [
        'views/view_disable_powered_odoo_footer.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': True,
}
