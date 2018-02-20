# -*- coding: utf-8 -*-

{
    'name': 'Project Issue Milestone',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Project',
    'summary': 'Create milestone to your project issues',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'project_issue',
        'project_task_milestone',
    ],
    'data': [
        'views/project_issue.xml',
        'views/project_milestone.xml',
    ],
    'installable': False,
}
