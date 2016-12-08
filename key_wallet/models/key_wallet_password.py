# -*- coding: utf-8 -*-
#    
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Michell Stuttgart <m.faria@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models


class ResPassword(models.Model):

    _name = 'key.wallet.password'
    _rec_name = 'title'
    _description = 'Represents password key'

    title = fields.Char(string='Title', required=True)
    url = fields.Char(string='URL')
    username = fields.Char(string='Username')
    password = fields.Char(string='Password')
    password_visible = fields.Char(string='Password', related='password')
    show_password = fields.Boolean(string='Show Password', default=False)
    description = fields.Html(string='Description')
    group_id = fields.Many2one('res.groups', string='Owner Group')
    category_ids = fields.Many2many('key.wallet.category', string='Category')

    create_date = fields.Datetime(index=True, string='Date', readonly=True)
    write_date = fields.Datetime(index=True, string='Date', readonly=True)

    create_uid = fields.Many2one('res.users', string='By', readonly=True,
                                 default=lambda self: self.env.uid)
    write_uid = fields.Many2one('res.users', string='By', readonly=True)

    @api.model
    def create(self, values):
        # values['show_password'] = False
        values.update({'show_password': False})
        return super(ResPassword, self).create(vals=values)

    @api.multi
    def write(self, values):
        values.update({'show_password': False})
        # values['show_password'] = False
        return super(ResPassword, self).write(vals=values)

    @api.onchange('password_visible')
    def onchange_password_visible(self):
        self.password = self.password_visible
