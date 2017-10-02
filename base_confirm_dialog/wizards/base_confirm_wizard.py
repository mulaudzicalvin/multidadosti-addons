# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ConfirmEventsWizard(models.TransientModel):
    _name = 'base.confirm.wizard'

    message = fields.Char(string='Message', readonly=True)

    wiz_model = fields.Char(string='Wizard Model', readonly=True)

    xml_id_action = fields.Char(string='XML ID Action', readonly=True)

    method = fields.Char(string='Method', readonly=True)

    @api.multi
    def yes(self):
        wiz_id = self.env.context.get('active_id')
        rec_wiz = self.env[self.wiz_model].browse([wiz_id])
        generated_records = getattr(rec_wiz, self.method)()

        res = self.env['ir.actions.act_window'].for_xml_id(
            *self.xml_id_action.split('.'))

        res['domain'] = [('id', 'in', generated_records)]

        return res

    @api.multi
    def no(self):
        return False

