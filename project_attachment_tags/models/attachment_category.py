# -*- coding: utf-8 -*-

from odoo import fields, models


class AttachCategoryLines(models.Model):

    _name = "attach.category.line"

    name = fields.Char(string='Name')


class AttachCategory(models.Model):

    _name = "attach.category"

    name = fields.Char(string='Name')

    line_ids = fields.Many2many(
        string='Tag',
        comodel_name='attach.category.line')
