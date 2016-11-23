# -*- coding: utf-8 -*-
#    Disable Support via Trustcode Footer to Odoo
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Aldo Soares <a.soares@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Disable Support by Trustcode footer',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'https://github.com/multidadosti-erp/multidadosti-addons',
    'summary': 'Disable \'Support by Trustcode\' footer',
    'category': 'Web',
    'depends': [
        'web',
        'br_base',
    ],
    'data': [
        'views/view_disable_support_odoo_footer.xml',
    ],
    'installable': True,
}
