# -*- coding: utf-8 -*-

{
    'name': 'General Calendar',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': """
        Merge calendars in a general calendar.
    """,
    'category': 'Sales',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'base',
        'calendar',
        'web_calendar_read_only',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/general_calendar.xml',
        'views/general_calendar.xml',
        'views/general_calendar_line.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
