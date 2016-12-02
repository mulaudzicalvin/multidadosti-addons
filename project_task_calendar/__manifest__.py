# -*- coding: utf-8 -*-
#    Multidados Project
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Aldo Soares <a.soares@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Project Task in Calendar',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'https://github.com/multidadosti-erp/multidadosti-addons',
    'summary': """Custom module developed for visual improvement on project
               module and integration with calendar Support by MultidadosTI""",
    'category': 'Project',
    'depends': [
        'project',
        'calendar',
        'document',
    ],
    'data': [
<<<<<<< 7a7be84492664280c9619ff064dde1466f74ee53:project_task_calendar/__manifest__.py
        'views/view_multi_project.xml',
        'views/view_project_project.xml',
=======
        'views/calendar_meeting.xml',
        'views/view_custom_menu_group.xml',

>>>>>>> [IMP] Implementação de menu customizado, agrupamento de calendario, post-it e mensagens:multi-project/__manifest__.py
    ],
    'installable': True,
}