# -*- coding: utf-8 -*-
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

    description_type = fields.Selection([('field', 'Field'),
                                         ('code', 'Code')],
                                        string="Description Type",
                                        default='field')

    description_field_id = fields.Many2one(
        comodel_name='ir.model.fields',
        string='Description field',
        domain="[('ttype', 'in', ('char', 'text')), "
               "('model_id', '=', name),"
               "('store', '=', True)]",
    )

    description_code = fields.Text(string='Description field',
                                   help=("""Use '${o}' to refer
                                   to the involved object.
                                   E.g.: '${o.project_id.name}'"""))

    date_start_field_id = fields.Many2one(
        comodel_name='ir.model.fields',
        string='Start date field',
        domain="[('ttype', 'in', ('datetime', 'date')), "
               "('model_id', '=', name),('store', '=', True)]",
        required=True,
    )

    date_stop_field_id = fields.Many2one(
        comodel_name='ir.model.fields',
        string='End date field',
        domain="[('ttype', 'in', ('datetime', 'date')),"
               "('model_id', '=', name),"
               "('store', '=', True)]",
    )

    all_day_field_id = fields.Many2one(
        comodel_name='ir.model.fields',
        string='All Day field',
        domain="[('ttype', '=', 'boolean'), ('model_id', '=', name)],"
               "('store', '=', True)",
    )

    user_field_id = fields.Many2one(
        comodel_name='ir.model.fields',
        string='User field',
        domain="[('ttype', '=', 'many2one'), ('model_id', '=', name)],"
               "('store', '=', True)",
    )

    @api.multi
    def get_details(self):

        select_str = []

        for index, line in enumerate(self.search([])):

            f_user = 'table_name.' + line.user_field_id.name \
                if line.user_field_id else 'NULL'

            f_date_start = 'table_name.' + line.date_start_field_id.name \
                if line.date_start_field_id else 'NULL'

            f_date_stop = 'table_name.' + line.date_stop_field_id.name \
                if line.date_stop_field_id else 'NULL'

            f_allday = 'table_name.' + line.all_day_field_id.name \
                if line.all_day_field_id else 'false'

            f_description = 'table_name.' + line.description_field_id.name \
                if line.description_field_id else 'false'

            table_name = line.name.model.replace('.', '_')

            select = """SELECT
                %s + table_name.id AS id,
                %s AS name,
                %s AS date_start,
                %s AS date_stop,
                %s AS allday,
                %s AS user_id,
                \'%s,\' || CAST(table_name.id AS varchar) AS res_id,
                %d AS model_id
                FROM
                    table_name """ % ((index + 1) * 1000000,
                                      f_description,
                                      f_date_start,
                                      f_date_stop,
                                      f_allday,
                                      f_user,
                                      line.name.model,
                                      line.name.id)

            select = select.replace('table_name', table_name)
            select_str.append(select)

        return select_str
