# -*- coding: utf-8 -*-

{
    'name': 'Project Team',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Project',
    'summary': 'Create teams to your projects',
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'project',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/project_project.xml',
        'views/project_team.xml',
    ],
    'installable': True,
}
