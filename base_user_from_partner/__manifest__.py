# -*- coding: utf-8 -*-

{
    'name': 'User From Partner',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Base',
    'summary': """This module add feature to select specific partner when
    a new user is create.""",
    'contributors': [
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
    ],
    'depends': [
        'base',
    ],
    'data': [
        'views/res_user_view.xml',
    ],
    'installable': True,
}