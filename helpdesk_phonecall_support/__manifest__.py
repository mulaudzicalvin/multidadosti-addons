# -*- coding: utf-8 -*-

{
    'name': 'PhoneCall Support',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': """Phonecall service to Odoo by MultidadosTI""",
    'category': 'Project',
    'contributors': [
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
    ],
    'depends': [
        'project_team',
        'hr_timesheet',
    ],
    'data': [
        'data/helpdesk_data.xml',
        'security/ir.model.access.csv',
        'security/helpdesk_phonecall_support.xml',
        'views/helpdesk_phonecall_service_view.xml',
        'wizard/wizard_helpdesk_phonecall_confirm_view.xml',
    ],
    'installable': True,
}
