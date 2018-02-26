from odoo import fields, models


class HelpDeskPhonecallServiceTag(models.Model):
    _name = 'helpdesk.phonecall.service.tag'

    name = fields.Char('Name')
