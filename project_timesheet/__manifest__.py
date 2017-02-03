# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

{
    'name': 'Project Timesheet',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'Michell Stuttgart <michellstut@gmail.com>',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Project',
    'summary': 'Project Improvements in Timesheet',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'hr_timesheet',
        'project_task_calendar',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/to_invoice_data.xml',
        'views/account_analytic_line_view.xml',
        'views/to_invoice_view.xml',
        'views/project_task.xml',
    ],
    'installable': True,
}
