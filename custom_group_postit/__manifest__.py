# -*- coding: utf-8 -*-
#    Custom Group Post-it
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Aldo Soares <a.soares@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Custom Group Post-it',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'https://github.com/multidadosti-erp/multidadosti-addons',
    'summary': 'Group calendar, productivity(post-it) and messages',
    'category': 'Web',
    'sequence': 99,
    'depends': [
        'project_task_calendar',
        'note',
    ],
    'data': [
        'views/view_custom_group_postit.xml',
    ],
    'installable': True,
}
