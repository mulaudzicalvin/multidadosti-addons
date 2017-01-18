# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
{
    'name': 'Jasper Report',
    'version': '10.0.1.0.0',
    'summary': 'Jasper Client',
    'category': 'Reports',
    'author': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/jasper_report_settings.xml',
        'views/act_report_xml_view.xml',
    ],
    'installable': True,
    'application': True,
}
