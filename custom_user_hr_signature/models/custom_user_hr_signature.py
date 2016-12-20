from odoo import models, fields


class CustomUserHRSignature(models.Model):
    _inherit = 'hr.employee'

    signature = fields.Binary("Assinatura",
                              attachment=True,
                              help="This field holds the image used as photo "
                                   "for the employee, limited to 1024x1024px.")
