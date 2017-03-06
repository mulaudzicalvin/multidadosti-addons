# -*- coding: utf-8 -*-

{
    'name': 'HR Timeshee Project Task Stage',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Timesheets',
    'summary': 'Use project task stage to filter stages in timesheet',
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'hr_timesheet',
    ],
    'data': [
        'views/account_analytic_line.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
