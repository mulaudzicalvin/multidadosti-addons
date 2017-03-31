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
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'project_related_partners',
        'calendar_event_partner',
        'calendar_event_stage',
    ],
    'data': [
        'views/calendar_event.xml',
        'views/project_project.xml',
        'views/project_task.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
