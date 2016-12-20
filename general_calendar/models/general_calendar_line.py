# -*- coding: utf-8 -*-
# General Calendar
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models


class CalendarLine(models.Model):

    _name = 'general.calendar.line'

    name = fields.Many2one(comodel_name='ir.model',
                           string='Model',
                           required=True)

    domain = fields.Char(string='Domain')

    # configurator_id = fields.Many2one(
    #     comodel_name='super.calendar.configurator',
    #     string='Configurator',
    # )
    description_type = fields.Selection([('field', 'Field'),
                                         ('code', 'Code')],
                                        string="Description Type",
                                        default='field')

    description_field_id = fields.Many2one(
        comodel_name='ir.model.fields',
        string='Description field',
        domain="[('ttype', 'in', ('char', 'text')), ('model_id', '=', name)]",
    )

    description_code = fields.Text(string='Description field',
                                   help=("""Use '${o}' to refer
                                   to the involved object.
                                   E.g.: '${o.project_id.name}'"""),
    )

    date_start_field_id = fields.Many2one(
        comodel_name='ir.model.fields',
        string='Start date field',
        domain="[('ttype', 'in', ('datetime', 'date')), "
               "('model_id', '=', name)]",
        required=True,
    )

    date_stop_field_id = fields.Many2one(
        comodel_name='ir.model.fields',
        string='End date field',
        domain="[('ttype', 'in', ('datetime', 'date')), "
               "('model_id', '=', name)]",
    )

    duration_field_id = fields.Many2one(
        comodel_name='ir.model.fields',
        string='Duration field',
        domain="[('ttype', '=', 'float'), ('model_id', '=', name)]",
    )

    all_day_field_id = fields.Many2one(
        comodel_name='ir.model.fields',
        string='All Day field',
        domain="[('ttype', '=', 'boolean'), ('model_id', '=', name)]",
    )

    user_field_id = fields.Many2one(
        comodel_name='ir.model.fields',
        string='User field',
        domain="[('ttype', '=', 'many2one'), ('model_id', '=', name)]",
    )

    @api.multi
    def get_details(self):

        # lines =
        select_str = []

        for index, line in enumerate(self.search([])):

            # for obj_calendar in self.env[line.name.model].search([]):
            f_user = 'table_name.' + line.user_field_id.name if line.user_field_id else 'NULL'
            f_descr = 'table_name.' + line.description_field_id.name if line.description_field_id else 'false'
            f_date_start = 'table_name.' + line.date_start_field_id.name if line.date_start_field_id else 'NULL'
            f_date_stop = 'table_name.' + line.date_stop_field_id.name if line.date_stop_field_id else 'NULL'
            f_duration = 'table_name.' + line.duration_field_id.name if line.duration_field_id else 0.00
            f_allday = 'table_name.' + line.all_day_field_id.name if line.all_day_field_id else 'false'
            table_name = line.name.model.replace('.', '_')

            select = """SELECT
                %s + table_name.id AS id,
                table_name.name AS name,
                %s AS date_start,
                %s AS date_stop,
                %s AS duration,
                %s AS allday,
                %s AS user_id,
                \'%s,\' || CAST(table_name.id AS varchar) AS res_id,
                %d AS model_id
                FROM
                    table_name """ % ((index + 1) * 1000000, f_date_start, f_date_stop, f_duration, f_allday, f_user, line.name.model, line.name.id)

            select = select.replace('table_name', table_name)

            select_str.append(select)

        return select_str
