# -*- coding: utf-8 -*-
# General Calendar
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'General Calendar',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': """
    Merge calendars in a general calendar Support by MultidadosTI
    """,
    'category': 'Project',
    'depends': [
        'base',
        'calendar',
    ],
    'data': [
        'views/web_calendar_templates.xml',
        'views/general_calendar_view.xml',
        'views/general_calendar_line_view.xml',
    ],
    'installable': True,
}
