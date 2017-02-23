# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'General Views Customize',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'General Views Customize',
    'category': 'Web',
    'sequence': 99,
    'description': """
        This module customize appearance of his dependencies
    """,
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'web_kanban',
        'br_base',
        'disable_odoo_online',
        'res_config_settings_enterprise_remove',
    ],
    'data': [
        'views/multi_assets.xml',
        'views/general_views_customize.xml',
        'views/res_partner_view.xml',
    ],
    'qweb': [
        'static/src/xml/dashboard.xml',
    ],
    'installable': True,
}
