# -*- coding: utf-8 -*-

{
    'name': 'Calendar Event - Disable Quick Create',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Project',
    'summary': """Disables quick create option in
                    calendar event at calendar view""",
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'calendar',
    ],
    'data': [
        'views/calendar_event.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
