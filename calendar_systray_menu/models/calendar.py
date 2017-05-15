from odoo import models


class Calendar(models.Model):
    _inherit = 'calendar.event'

    def get_id_menu(self):
        return self.env.ref('calendar.mail_menu_calendar')
