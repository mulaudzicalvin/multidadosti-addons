{
    'name': 'Account Move Backup',
    'version': '11.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Account',
    'summary': 'This module makes a backup of deleted move line records',
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
    ],
    'depends': [
        'br_account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_backup.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
