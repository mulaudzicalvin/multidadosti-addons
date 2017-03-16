# -*- coding: utf-8 -*-

{
    'name': 'Mail - Custom Menu Location',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'Customizes menus from mail',
    'category': 'Web',
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
    ],
    'depends': [
        'menu_groups',
        'mail',
    ],
    'data': [
        'views/mail_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
