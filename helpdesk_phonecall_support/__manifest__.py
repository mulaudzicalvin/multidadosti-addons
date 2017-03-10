# -*- coding: utf-8 -*-

{
    'name': 'PhoneCall Support',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': """Add feature of phonecall service""",
    'category': 'Project',
    'contributors': [
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
    ],
    'depends': [
        'project_team',
        'project_related_partners',
    ],
    'data': [
        'data/helpdesk_phonecall_service_tag.xml',
        'security/ir.model.access.csv',
        'security/helpdesk_phonecall_service.xml',
        'views/helpdesk_phonecall_service.xml',
        'wizards/helpdesk_phonecall_confirm.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
