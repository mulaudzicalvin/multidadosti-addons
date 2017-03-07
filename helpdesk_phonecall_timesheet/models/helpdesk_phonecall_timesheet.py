# -*- coding: utf-8 -*-

from odoo.exceptions import UserError
from odoo import api, fields, models, _


class HelpTime(models.Model):
    _name = 'wizard.helpdesk.timesheet.create'
    _description = 'Wizard to confirm phonecall'


@api.multi
def action_finish_phonecall(self):
    return {
        'type': 'ir.actions.act_window',
        'res_model': 'wizard.helpdesk.timesheet.create',
        'view_type': 'form',
        'view_mode': 'form',
        'views': [(False, "form")],
        'target': 'new', }
