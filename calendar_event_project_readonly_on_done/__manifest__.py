{
    'name': 'Calendar Event Project Readonly on Done',
    'version': '11.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Extra Tools',
    'summary': 'Make project and task readonly when calendar event is done',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'project_task_calendar',
    ],
    'data': [
        'views/calendar_event.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
