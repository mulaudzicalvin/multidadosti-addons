from odoo import fields, models


class AttachCategory(models.Model):

    _name = 'attach.category'

    name = fields.Char(string='Name', required=True)

    tag_ids = fields.Many2many(comodel_name='attach.category.tag',
                               required=True,
                               string='Tags')


class AttachCategoryTag(models.Model):

    _name = 'attach.category.tag'

    name = fields.Char(string='Name', required=True)
