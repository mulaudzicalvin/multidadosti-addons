# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Project Task in Calendar',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': """Custom module developed for visual improvement on project
               module and integration with calendar Support by MultidadosTI""",
    'category': 'Project',
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
        'Michell Stuttgart <michellstut@gmail.com>',
        'Rodrigo Ferreira <rodrigo.santos@multidadosti.com.br>',
    ],
    'depends': [
        'project',
        'calendar',
        'hr_timesheet',
        'project_team',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/to_invoice_data.xml',
        'views/view_calendar.xml',
        'views/view_project_project.xml',
        'views/view_project_task.xml',
        'views/to_invoice_view.xml',
        'views/account_analytic_line_view.xml',
        'wizard/wizard_calendar_event_done.xml',
    ],
    'installable': True,
}
