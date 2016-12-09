# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <m.faria@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models


class KeyWalletPassword(models.Model):

    _name = 'key.wallet.password'
    _rec_name = 'title'
    _description = 'Represents password key'

    @api.model
    def _get_user_group_list(self):
        groups_id = self.env.user.groups_id
        groups_id_list = groups_id.ids if groups_id else []
        return [('id', 'in', groups_id_list)]

    title = fields.Char(string='Title', required=True)
    url = fields.Char(string='URL')
    username = fields.Char(string='Username')
    password = fields.Char(string='Password')
    password_visible = fields.Char(string='Password', related='password')
    show_password = fields.Boolean(string='Show Password', default=False)
    description = fields.Html(string='Description')
    group_id = fields.Many2one('res.groups', string='Owner Group',
                               domain=_get_user_group_list)
    category_ids = fields.Many2many('key.wallet.category', string='Category')

    create_date = fields.Datetime(index=True, string='Date', readonly=True)
    write_date = fields.Datetime(index=True, string='Date', readonly=True)

    create_uid = fields.Many2one('res.users', readonly=True)
    write_uid = fields.Many2one('res.users', readonly=True)

    @api.model
    def create(self, values):
        values.update({'show_password': False})
        return super(KeyWalletPassword, self).create(vals=values)

    @api.multi
    def write(self, values):
        values.update({'show_password': False})
        return super(KeyWalletPassword, self).write(vals=values)

    @api.onchange('password_visible')
    def onchange_password_visible(self):
        self.password = self.password_visible
