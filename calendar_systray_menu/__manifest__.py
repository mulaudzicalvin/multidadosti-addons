{
    'name': 'Calendar Systray Menu',
    'version': '11.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Extra Tools',
    'summary': 'This Module creates a widget in navbar that links to calendar '
               'views.',
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
        'Rodrigo Ferreira <rodrigosferreira91@gmail.com>',
    ],
    'depends': [
        'web',
        'calendar',
    ],
    'data': [
        'views/web_templates.xml',
    ],
    'qweb': [
        'static/src/xml/systray.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
