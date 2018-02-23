from odoo import fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    send_quotation = fields.Boolean(string='Send Quotation',
                                    related='stage_id.allow_quotation',
                                    readonly=True)
