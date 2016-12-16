# -*- coding: utf-8 -*-
# General Calendar
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


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

    user_field_id = fields.Many2one(
        comodel_name='ir.model.fields',
        string='User field',
        domain="[('ttype', '=', 'many2one'), ('model_id', '=', name)]",
    )
