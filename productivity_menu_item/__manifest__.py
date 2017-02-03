# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

{
    'name': 'Productivity Menu Item',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'Group calendar, productivity(post-it) and messages',
    'category': 'Web',
    'sequence': 99,
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'general_calendar',
        'note',
        'mail',
    ],
    'data': [
        'views/view_productivity_menu_item.xml',
    ],
    'qweb': [
        'static/src/xml/client_action.xml'
    ],
    'installable': True,
}
