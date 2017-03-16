# -*- coding: utf-8 -*-

{
    'name': 'Calendar Read Only',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': """
        Sets status read-only to Calendar.
    """,
    'category': 'Sales',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'calendar',
    ],
    'data': [
        'templates/web_calendar.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
