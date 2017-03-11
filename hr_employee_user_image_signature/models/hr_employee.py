# -*- coding: utf-8 -*-

from odoo import models, fields


class CustomUserHRSignature(models.Model):

    _inherit = 'hr.employee'

    image_signature = fields.Binary(string="Signature",
                                    help="This field holds the image used as "
                                         "signature for the employee, limited "
                                         "to 1024x1024px. It can be used in "
                                         "reports.")
