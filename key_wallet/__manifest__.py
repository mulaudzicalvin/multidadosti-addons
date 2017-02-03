# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Key Wallet',
    'version': '10.0.1.0.0',
    'summary': 'Password manager',
    'category': 'Key Wallet',
    'author': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'base',
    ],
    'data': [
        'security/key_wallet_security.xml',
        'security/ir.model.access.csv',
        'views/view_key_wallet_password.xml',
        'views/view_key_wallet_category.xml',
    ],
    'application': True,
}
