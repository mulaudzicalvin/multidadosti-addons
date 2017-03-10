# -*- coding: utf-8 -*-

{
    'name': 'Project Task in Calendar',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': """Add Project and Project Task relation in Calendar Events""",
    'category': 'Project',
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'project_related_partners',
        'calendar_event_partner',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        # 'data/to_invoice_data.xml',
        'views/calendar_event.xml',
        'views/project_project.xml',
        'views/project_task.xml',
        # 'views/to_invoice_view.xml',
        # 'views/account_analytic_line_view.xml',
        # 'wizard/wizard_calendar_event_done.xml',
    ],
    'installable': True,
}
