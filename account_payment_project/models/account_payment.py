from odoo import fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    project_id = fields.Many2one(string='Project',
                                 comodel_name='project.project')
