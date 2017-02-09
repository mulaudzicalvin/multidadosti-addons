# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Rodrigo Ferreira <rodrigosferreira91@gmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

from odoo import api, fields, models


class HelpDeskPhoneCall(models.Model):
    _name = 'helpdesk.phonecall.service'

    name = fields.Text(string='Description')

    start_date_hour = fields.Datetime(string='Start Date',
                                      readonly=True,
                                      default=lambda s: fields.Datetime.now())

    partner_id = fields.Many2one(string='Partner',
                                 comodel_name='res.partner')

    project_id = fields.Many2one(comodel_name='project.project')

    contact_partner_id = fields.Many2one(string='Contact',
                                         comodel_name='res.partner')

    user_id = fields.Many2one('res.users', string='User', readonly=True,
                              default=lambda self: self._uid)

    finish_date_hour = fields.Datetime(string='Finish Date',
                                       readonly=True, )

    solicitation = fields.Selection(string='Solicitation', selection=(
        [('1', u'Dúvidas Gerais'),
         ('2', u'Dúvidas Nota Fiscal'), ('3', u'Erro NFe'),
         ('4', u'Erro NFSe'), ('5', u'Erro VMulti'), ('6', u'Nova Solicitação')]))

    def button_finish_data(self):
        self.finish_date_hour = fields.Datetime.now()
