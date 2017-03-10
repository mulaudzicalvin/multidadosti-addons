# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProjectProject(models.Model):
    _inherit = 'project.project'

    partner_ids = fields.Many2many(comodel_name='res.partner',
                                   string='Related Partners')

    @api.model
    def create(self, values):
        # Copy partner_id to partner_ids field
        if 'partner_ids' in values:
            if not values['partner_ids']:
                values['partner_ids'] = [(4, values['partner_id'])]
            else:
                values['partner_ids'][0][2].append(values['partner_id'])

        return super(ProjectProject, self).create(values)

    @api.multi
    def write(self, values):
        # Copy partner_id to partner_ids field
        if 'partner_id' not in values and self.partner_id:
            values['partner_id'] = self.partner_id.id

        if 'partner_id' in values:
            if 'partner_ids' not in values:
                values['partner_ids'] = [(4, values['partner_id'])]
            else:
                values['partner_ids'][0][2].append(values['partner_id'])

        return super(ProjectProject, self).write(values)
