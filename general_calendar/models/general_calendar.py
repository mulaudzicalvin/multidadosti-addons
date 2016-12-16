# -*- coding: utf-8 -*-
# General Calendar
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models, tools


def _models_get(self):
    model_obj = self.env['ir.model']
    model_list = model_obj.search([])
    return [(model.model, model.name) for model in model_list]


class GeneralCalendar(models.Model):

    _name = 'general.calendar'
    _auto = False

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

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)

        lines = self.env['general.calendar.line'].search([])

        select_str = []

        for line in lines:
            obj_calendar = self.env[line.name.model].search([])
            f_user = obj_calendar.user_field_id.name
            f_descr = obj_calendar.description_field_id.name
            f_date_start = obj_calendar.date_start_field_id.name
            f_date_stop = obj_calendar.date_stop_field_id.name
            f_duration = obj_calendar.duration_field_id.name

            select = """SELECT
                t.id as id,
                'teste' as name,
                %s as date_start,
                %s as duration,
                %s as user_id,
                NULL as res_id,
                NULL as model_id
                FROM
                    %s t""" % (self.self.env[line.name.model]._table, f_date_start, f_duration, f_user)

            select_str.append(select)

        sel = ''
        for select in select_str:


        sql = """CREATE VIEW %s AS
               SELECT
                    line.id as id,
                    'teste' as name,
                    line.date_start_field_id as date_start,
                    line.duration_field_id as duration,
                    line.user_field_id as user_id,
                    NULL as res_id,
                    NULL as model_id
               FROM
                    general_calendar_line line""" % self._table

        self.env.cr.execute(sql)
