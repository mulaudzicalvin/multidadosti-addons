# -*- coding: utf-8 -*-
#    Geo localization to Brazil Localization to Odoo
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Michell Stuttgart <m.faria@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Geo-Localization to Brazil',
    'version': '8.0.1.0.0',
    'description': 'Partners Geo-Localization to Brazil',
    'summary': 'Geo localization to Brazil Localization',
    'category': 'Customer Relationship Management',
    'author': 'MultidadosTI',
    'website': 'https://github.com/multidadosti-erp/multidadosti-addons',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'l10n_br_zip_correios',
        'base_geolocalize',
    ],
    'test': [
        'test/res_partner.yml',
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'auto_install': True,
}
