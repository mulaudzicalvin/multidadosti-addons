# -*- coding: utf-8 -*-

import datetime

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class WizardHelpDeskTimesheetCreate(models.TransientModel):
    _name = 'wizard.helpdesk.timesheet.create'
    _description = 'Wizard to create timesheet'

    @api.multi
    def action_create_timesheet(self):
        print 'classe filha'
        ret = super(WizardHelpDeskTimesheetCreate, self).action_create_timesheet()
        # dt = datetime.datetime.strptime(rec.start_date_hour,
        #                                 '%Y-%m-%d %H:%M:%S')
        #
        # fmt = '%Y-%m-%d %H:%M:%S'
        # d1 = datetime.datetime.strptime(rec.start_date_hour, fmt)
        # d2 = datetime.datetime.strptime(rec.finish_date_hour, fmt)
        #
        # # Convert total seconds in hours in decimal format
        # # When load the float field in screen, the widget
        # # 'float_time' will go show time in to HH:MM format
        # hours_diff_decimal = (d2 - d1).total_seconds() / 3600.0
        #
        # values = {
        #     'name': rec.description,
        #     'date': dt.date(),
        #     'user_id': rec.user_id.id,
        #     'project_id': rec.project_id.id,
        #     'unit_amount': hours_diff_decimal,
        # }
        #
        # self.env['account.analytic.line'].create(values)

        return ret

