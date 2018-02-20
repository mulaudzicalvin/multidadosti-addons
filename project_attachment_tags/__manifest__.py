# -*- coding: utf-8 -*-

{
    'name': 'Project Attachment Category Tags',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Project',
    'summary': 'Adds category field, and tag field in your attachment project',
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
    ],
    'depends': [
        'project',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/ir_attachment.xml',
        'views/attachment_category.xml',
        'views/project_project.xml',
    ],
    'installable': False,
    'auto_install': False,
    'application': False,
}
