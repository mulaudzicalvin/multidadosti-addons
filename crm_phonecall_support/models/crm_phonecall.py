# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Rodrigo Ferreira <rodrigosferreira91@gmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, fields, models


class PhoneCallCrm(models.Model):

    _name = 'phonecall.service'

    name = fields.Text(string='Description')

    start_date_hour = fields.Datetime(string='Start Date')

    partner_id = fields.Many2one(string='Partner',
                              comodel_name='res.partner')

    project_id = fields.Many2one(comodel_name='project.project')

    contact_partner_id = fields.Many2one(string='Contact',
                              comodel_name='res.partner')

    user_id = fields.Many2one(string='User',
                              comodel_name='res.users')

    finish_date_hour = fields.Datetime(string='Finish Date')



