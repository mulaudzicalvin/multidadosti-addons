# -*- coding: utf-8 -*-
#    
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Michell Stuttgart <m.faria@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class ResPassword(models.Model):

    _name = 'res.password'
    _rec_name = 'title'
    _description = 'Represents password key'

    title = fields.Char(string='Title')
    url = fields.Char(string='URL')
    username = fields.Char(string='Username')
    password = fields.Char(string='Password')
    description = fields.Html(string='Description')
    group_id = fields.Many2one('res.groups', string='Owner Group')
    category_id = fields.Many2one('res.password.category', string='Category')

    create_date = fields.Datetime(index=True, string='Date', readonly=True)
    write_date = fields.Datetime(index=True, string='Date', readonly=True)

    create_uid = fields.Many2one('res.users', string='By', readonly=True,
                                 default=lambda self: self.env.uid)
    write_uid = fields.Many2one('res.users', string='By', readonly=True)


class ResPasswordCategory(models.Model):

    _name = 'res.password.category'
    _description = 'Password Category'

    name = fields.Char(string='Name', required=True)
    res_password_ids = fields.One2many('res.password', 'category_id',
                                       string='Passwords')
