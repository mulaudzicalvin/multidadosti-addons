# -*- coding: utf-8 -*-

{
    'name': 'Project Task - Create and Count Meetings',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Project',
    'summary': """Count meeting records at kanban view and
                creates new meetings from project's task view form""",
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'calendar',
        'project',
        'project_task_calendar',
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
