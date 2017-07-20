# -*- coding: utf-8 -*-

from odoo import api, fields, models


class IrAttachment(models.Model):

    _inherit = "ir.attachment"

    tag_id = fields.Many2one(comodel_name='attach.category.tag',
                             string='Tag')

    @api.onchange('res_id')
    def _onchange_res_id(self):
        # TODO Corrigir uso do domain quando o record é editado
        if self.res_model == 'project.project':
            category_id = self.env['project.project'].browse(
                self.res_id).attachment_category_id
        else:
            category_id = False

        tag_ids = category_id.tag_ids.ids if category_id else []
        return {'domain': {'tag_id': [('id', 'in', tag_ids)]}}
