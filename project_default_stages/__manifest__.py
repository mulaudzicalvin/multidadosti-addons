{
    'name': 'Project Default Stages',
    'version': '11.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Project',
    'summary': 'This Module allows create projects without default stages',
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'project_task_default_stage',
    ],
    'data': [
        'views/project_project.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
