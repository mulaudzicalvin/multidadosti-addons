# -*- coding: utf-8 -*-

{
    'name': 'Project Task Milestone',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Project',
    'summary': 'Create milestone to your project tasks',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'project',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/project_task.xml',
        'views/project_milestone.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
