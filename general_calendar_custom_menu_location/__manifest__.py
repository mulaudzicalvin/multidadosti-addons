# -*- coding: utf-8 -*-

{
    'name': 'General Calendar - Custom Menu Location',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'Customizes menus from general calendar',
    'category': 'Web',
    'sequence': 99,
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
    ],
    'depends': [
        'menu_groups',
        'general_calendar',
    ],
    'data': [
        'views/general_calendar_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
