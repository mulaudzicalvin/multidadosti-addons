# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Rodrigo Ferreira <rodrigosferreira91@gmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

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
        'project',
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
