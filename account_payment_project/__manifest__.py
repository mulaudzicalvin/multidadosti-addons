# -*- coding: utf-8 -*-

{
    'name': 'Account Payment - Defines a relation between account.payment and '
            'project.project',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Account',
    'summary': """This module defines a relation between account.payment and
                project.project""",
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
    ],
    'depends': [
        'general_payments',
        'project_related_partners',
    ],
    'data': [
        'views/account_payment.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
