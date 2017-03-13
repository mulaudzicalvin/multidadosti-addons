# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    @api.multi
    def get_company_partner(self):
        company_id = \
            self.env['res.company']._company_default_get('calendar.event')

        return company_id.partner_id

    partner_id = fields.Many2one(comodel_name='res.partner',
                                 string='Partner')

    company_partner_id = fields.Many2one(comodel_name='res.partner',
                                         default=get_company_partner)
