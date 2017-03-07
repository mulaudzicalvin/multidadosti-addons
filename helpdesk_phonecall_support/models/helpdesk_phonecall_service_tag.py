# -*- coding: utf-8 -*-

from odoo import fields, models


class HelpDeskPhonecallServiceTag(models.Model):
    _name = 'heldpesk.phonecall.service.tag'

    name = fields.Char('Name')
