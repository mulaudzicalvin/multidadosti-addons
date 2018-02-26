from odoo import fields, models


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    calendar_event_id = fields.Many2one(comodel_name='calendar.event',
                                        readonly=True,
                                        string='Calendar Event')
