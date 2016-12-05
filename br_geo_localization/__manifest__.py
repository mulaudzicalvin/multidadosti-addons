# -*- coding: utf-8 -*-
#    Geo localization to Brazil Localization to Odoo
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Michell Stuttgart <m.faria@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Geo-Localization to Brazil',
    'version': '10.0.1.0.0',
    'summary': 'Geo localization to Brazil Localization',
    'category': 'Customer Relationship Management',
    'author': 'MultidadosTI',
    'website': 'https://github.com/multidadosti-erp/multidadosti-addons',
    'license': 'AGPL-3',
    'depends': [
        'br_zip',
        'base_geolocalize',
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
    'installable': True,
}
