# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <m.faria@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import datetime

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class WizardHelpDeskPhoneCallConfirm(models.TransientModel):

    _name = 'wizard.helpdesk.phonecall.confirm'
    _description = 'Wizard to confirm phonecall'

    @api.multi
    def confirm_finish_phonecall(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []

        for rec in self.env['helpdesk.phonecall.service'].browse(active_ids):
            if rec.state != 'open':
                raise UserError(_("Selected phonecalls cannot be confirmed "
                                  "as they are not in 'Open' state."))
            rec.finish_date_hour = fields.Datetime.now()
            rec.state = 'done'

            dt = datetime.datetime.strptime(rec.start_date_hour,
                                            '%Y-%m-%d %H:%M:%S')

            fmt = '%Y-%m-%d %H:%M:%S'
            d1 = datetime.datetime.strptime(rec.start_date_hour, fmt)
            d2 = datetime.datetime.strptime(rec.finish_date_hour, fmt)

            # Convert total seconds in hours in decimal format
            # When load the float field in screen, the widget
            # 'float_time' will go show time in to HH:MM format
            hours_diff_decimal = (d2 - d1).total_seconds() / 3600.0

            values = {
                'name': rec.description,
                'date': dt.date(),
                'user_id': rec.user_id.id,
                'project_id': rec.project_id.id,
                'unit_amount': hours_diff_decimal,
            }

            self.env['account.analytic.line'].create(values)

        return {'type': 'ir.actions.act_window_close'}
