# -*- coding: utf-8 -*-

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
        'calendar_event_partner_readonly_on_done',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        # 'data/to_invoice_data.xml',
        'views/view_calendar.xml',
        'views/view_project_project.xml',
        'views/view_project_task.xml',
        # 'views/to_invoice_view.xml',
        # 'views/account_analytic_line_view.xml',
        # 'wizard/wizard_calendar_event_done.xml',
    ],
    'installable': True,
}
