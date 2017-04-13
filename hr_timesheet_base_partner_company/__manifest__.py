# -*- coding: utf-8 -*-

{
    'name': 'HR Timesheet - Base Partner and Company',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': """This module adds the collumns partner_id and
            company_id in tree view of module account_analytic_line.""",
    'category': 'Timesheets',
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
    ],
    'depends': [
        'hr_timesheet',
        'sale_timesheet',
        'helpdesk_phonecall_support',
    ],
    'data': [
        'views/account_analytic_line.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
