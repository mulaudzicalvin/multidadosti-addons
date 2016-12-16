# -*- coding: utf-8 -*-
# General Calendar
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


def _models_get(self):
    model_obj = self.env['ir.model']
    model_list = model_obj.search([])
    return [(model.model, model.name) for model in model_list]


class GeneralCalendar(models.Model):

    _name = 'general.calendar'

    name = fields.Char(
        string='Description',
        required=True,
        readonly=True,
    )
    date_start = fields.Datetime(
        string='Start date',
        required=True,
        readonly=True,
    )
    duration = fields.Float(
        string='Duration',
        readonly=True,
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        readonly=True,
    )
    # general_calendar_id = fields.Many2one(
    #     comodel_name='general.calendar.configurator',
    #     string='Configurator',
    #     readonly=True,
    # )
    res_id = fields.Reference(
        selection=_models_get,
        string='Resource',
        readonly=True,
    )
    model_id = fields.Many2one(
        comodel_name='ir.model',
        string='Model',
        readonly=True,
    )
