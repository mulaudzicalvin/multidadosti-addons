# -*- coding: utf-8 -*-
#    Custom Timesheet
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Aldo Soares <soares_aldo@hotmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Custom Timesheet',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'https://github.com/multidadosti-erp/multidadosti-addons',
    'summary': 'Custom Timesheet',
    'category': 'Project',
    'description': """
        Custom module for customize hr_timesheet module
        Changes:
            - progress bar field
            - *enterprises*
    """,
    'sequence': 99,
    'depends': [
        'hr_timesheet',
        'hr_timesheet_sheet',
    ],
    'data': [
        'views/view_custom_hr_timesheet.xml',
    ],
    'installable': True,
}
