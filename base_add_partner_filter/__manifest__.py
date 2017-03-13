# -*- coding: utf-8 -*-

{
    'name': 'Add Partner Filter',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'Add Partner Filter',
    'category': 'Web',
    'sequence': 99,
    'description': """
        This module adds new filter in res_partner views
    """,
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'base',
    ],
    'data': [
        'views/res_partner.xml',
    ],
    'installable': True,
}
