# -*- coding: utf-8 -*-

{
    'name': 'HR Timesheet - Hide Menus',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Timesheets',
    'summary': 'Make some menu items invisible',
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
    ],
    'depends': [
        'hr_timesheet_attendance',
        'hr_timesheet_sheet',
    ],
    'data': [
        'security/hr_timesheet.xml',
        'views/hr_timesheet.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
