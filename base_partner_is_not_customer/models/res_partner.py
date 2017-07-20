# -*- coding: utf-8 -*-


from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    is_company = fields.Boolean(default=True)
