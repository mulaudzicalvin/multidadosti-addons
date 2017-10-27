# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    activity_branch = fields.Many2one('partner.activity.branch',
                                      'Activity Branch')
