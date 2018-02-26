from odoo import api, fields, models, _
from odoo.exceptions import UserError


class HelpDeskPhoneCallConfirm(models.TransientModel):
    _name = 'helpdesk.phonecall.confirm'
    _description = 'Wizard to confirm phonecall'

    @api.multi
    def action_confirm_finish_phonecall(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []

        for rec in self.env['helpdesk.phonecall.service'].browse(active_ids):
            if rec.state != 'open':
                raise UserError(_("Selected phonecalls cannot be confirmed "
                                  "as they are not in 'Open' state."))
            rec.finish_date_hour = fields.Datetime.now()
            rec.state = 'done'

        return {'type': 'ir.actions.act_window_close'}
