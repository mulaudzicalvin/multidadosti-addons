# -*- coding: utf-8 -*-

from odoo import api, fields, models


class IrAttachment(models.Model):

    _inherit = "ir.attachment"

    category_id = fields.Many2one(comodel_name='attach.category',
                                  string='Category')

    tag_id = fields.Many2one(comodel_name='attach.category.line',
                             string='Tag')

    @api.onchange('res_id')
    def _onchange_category(self):
        if self.res_model == 'project.project':
            self.category_id = self.env['project.project'].browse(
                self.res_id).attachment_category

        lista_ids = self.category_id.line_ids.ids if self.category_id else []
        domain = {'domain': {'tag_id': [('id', '=', lista_ids)]}}
        return domain
