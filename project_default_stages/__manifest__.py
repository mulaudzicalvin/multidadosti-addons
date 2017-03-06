# -*- coding: utf-8 -*-

{
    'name': 'Project Default Stages',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Project',
    'summary': 'Allow create projects with default stages',
    'depends': [
        'project',
    ],
    'data': [
        'views/project_project.xml',
        'views/project_task_type.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
