# -*- coding: utf-8 -*-

{
    'name': 'Custom Dashboard',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'Custom Dashboard',
    'category': 'Web',
    'description': """
        This module customize appearance of dashboard
    """,
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'web_kanban',
    ],
    'qweb': [
        'static/src/xml/dashboard.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
