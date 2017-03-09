# -*- coding: utf-8 -*-

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
        This module customize web base module
    """,
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'web_add_partner_filter',
        'web_custom_dashboard',
        'web_custom_dialogs',
        'web_custom_login_page',
        'web_set_title_page',
        'disable_odoo_online',
        'res_config_settings_enterprise_remove',
    ],
    'installable': True,
}
