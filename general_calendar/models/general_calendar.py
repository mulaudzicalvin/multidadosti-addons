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
    allday = fields.Boolean(
        string='All Day',
        readonly=True,
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        readonly=True)

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

        select_str = self.env['general.calendar.line'].get_details()

        sql = 'CREATE VIEW %s AS \n' % self._table
        for select in select_str[:1]:
            sql += select + '\nUNION\n'

        for select in select_str[1:-1]:
            sql += select + '\nUNION\n'

        sql += select_str[-1] + ';'

        # sql = """CREATE VIEW %s AS
        #                SELECT   ce.id as id,
        #                         ce.name as name,
        #                         ce.start as date_start,
        #                         ce.duration as duration,
        #                         ce.user_id as user_id,
        #                         ce.allday as allday,
        #                         'calendar.event,' || CAST(ce.id AS varchar) AS res_id,
        #                         NULL as model_id
        #                FROM calendar_event ce
        #                WHERE ce.active = 'true'
        #                """ % self._table

        self.env.cr.execute(sql)
