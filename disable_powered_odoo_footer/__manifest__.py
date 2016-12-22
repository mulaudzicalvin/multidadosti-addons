# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Disable Powered by Odoo Footer',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'Disable \'powered by Odoo\' footer',
    'category': 'Web',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'web',
    ],
    'data': [
        'views/view_disable_powered_odoo_footer.xml',
    ],
    'installable': True,
}
