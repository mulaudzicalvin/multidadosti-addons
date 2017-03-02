# -*- coding: utf-8 -*-

{
    'name': 'Partner Is Not Customer',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Base',
    'summary': """This module set default value of \'customer\' field
    from \'res.partner\' model like False.""",
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'base',
    ],
    'data': [
        'views/res_partner_view.xml',
        'views/res_users_view.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}
