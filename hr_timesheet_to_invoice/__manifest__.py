# -*- coding: utf-8 -*-

{
    'name': 'HR Timesheet to Invoice',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Timesheets',
    'summary': 'Allow check a timesheet record will be invoiced or not',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'hr_timesheet',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/account_analytic_line_to_invoice.xml',
        'views/account_analytic_line_view.xml',
        'views/account_analytic_line_to_invoice.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
