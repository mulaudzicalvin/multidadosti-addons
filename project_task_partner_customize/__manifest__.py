{
    'name': 'Project Task Partner Customize',
    'version': '11.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Project',
    'summary': 'Replace partner field on project task screen',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'project_task_code',
        'project_related_partners',
    ],
    'data': [
        'views/project_task.xml',
        'views/project_project.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
