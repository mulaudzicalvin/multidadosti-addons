# -*- coding: utf-8 -*-

{
    'name': 'Calendar Event Stage',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Extra Tools',
    'summary': 'Add stage to your calendar events',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
        'Rodrigo Ferreira <rodrigo.santos@multidadosti.com.br>',
    ],
    'depends': [
        'calendar',
    ],
    'data': [
        'views/calendar_event.xml',
        'wizards/calendar_event_finish.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
