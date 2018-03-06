{
    'name': 'Project Task - Set Default Filter',
    'version': '11.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Project',
    'summary': 'Sets the default filter in project task module',
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
    ],
    'depends': [
        'project',
        'project_task_code',
    ],
    'data': [
        'views/project_task.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
