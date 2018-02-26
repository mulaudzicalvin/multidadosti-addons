{
    'name': 'Project Systray Progressbar',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '11.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': 'Project Systray Progressbar',
    'category': 'Web',
    'description': """
       This module hides the progress bar on the projects screen
    """,
    'contributors': [
        'Rodrigo Ferreira   <rodrigosferreira91@gmail.com>',
    ],
    'depends': [
        'project',
        'web_planner',
    ],
    'qweb': [
        'static/src/xml/web.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
