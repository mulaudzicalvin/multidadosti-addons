# -*- coding: utf-8 -*-

{
    'name': 'HelpDesk PhoneCall Timesheet',
    'license': 'LGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': """Integration PhoneCall and Timesheet""",
    'category': 'Project',
    'contributors': [
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
    ],
    'depends': [
        'helpdesk_phonecall_support',
        'hr_timesheet',
    ],
    'data': [
        'wizards/helpdesk_phonecall_confirm.xml',
    ],
    'installable': True,
}
