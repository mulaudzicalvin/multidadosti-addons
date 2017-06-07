# -*- coding: utf-8 -*-

from odoo import fields, models


class AttachCategoryLines(models.Model):

    _name = "attach.category.line"

    name = fields.Char(string='Name', required=True)


class AttachCategory(models.Model):

    _name = "attach.category"

    name = fields.Char(string='Name', required=True)

    line_ids = fields.Many2many(
        string='Tag',
        required=True,
        comodel_name='attach.category.line')
