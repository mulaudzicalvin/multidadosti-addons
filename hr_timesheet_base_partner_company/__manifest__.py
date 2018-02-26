{
    'name': 'HR Timesheet - Base Partner and Company',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '11.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': """This module adds the columns partner_id and
            company_id in tree view of module account_analytic_line.""",
    'category': 'Timesheets',
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'hr_timesheet',
    ],
    'data': [
        'views/account_analytic_line.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
