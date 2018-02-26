{
    'name': 'User From Partner',
    'version': '11.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Base',
    'summary': """This module add feature to select specific partner when
    a new user is create.""",
    'contributors': [
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
    ],
    'depends': [
        'base',
    ],
    'data': [
        'views/res_users.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
