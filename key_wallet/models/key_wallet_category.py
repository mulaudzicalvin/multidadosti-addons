# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <m.faria@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class ResPasswordCategory(models.Model):

    _name = 'key.wallet.category'
    _description = 'Password Category'

    name = fields.Char(string='Name', required=True)
    res_password_ids = fields.Many2many('key.wallet.password',
                                        string='Passwords',
                                        readonly=True)
