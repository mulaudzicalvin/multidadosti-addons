# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <m.faria@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class WizardHelpDeskPhoneCallConfirm(models.TransientModel):

    _name = 'wizard.helpdesk.phonecall.confirm'
    _description = 'Wizard to confirm phonecall'

    @api.multi
    def confirm_finish_phonecall(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []

        for record in self.env['helpdesk.phonecall.service'].browse(
                active_ids):

            if record.state != 'open':
                raise UserError(_("Selected phonecalls cannot be confirmed "
                                  "as they are not in 'Open' state."))
                
            record.finish_date_hour = fields.Datetime.now()
            record.state = 'done'

        return {'type': 'ir.actions.act_window_close'}
