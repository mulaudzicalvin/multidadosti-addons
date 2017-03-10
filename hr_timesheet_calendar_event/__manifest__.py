# -*- coding: utf-8 -*-

{
    'name': 'HR Timesheet - Relation Calendar Event',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Project',
    'summary': 'Sets a relation with calendar events',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'calendar',
        'hr_timesheet',
    ],
    'data': [
        'views/account_analytic_line.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
