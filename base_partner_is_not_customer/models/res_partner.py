# -*- coding: utf-8 -*-


from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    is_company = fields.Boolean(string='Is a Company', default=True,
                                help="Check if the contact is a company, "
                                     "otherwise it is a person")
