# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountMoveBackup(models.Model):
    _inherit = 'account.move'
    _name = 'account.move.backup'

    line_ids = fields.One2many(comodel_name='account.move.backup.line')

    @api.model
    def create(self, vals):
        return super(models.Model, self).create(vals)


class AccountMoveBackupLine(models.Model):
    _inherit = 'account.move.line'
    _name = 'account.move.backup.line'

    move_id = fields.Many2one(comodel_name='account.move.backup')

    @api.model
    def create(self, vals):
        return super(models.Model, self).create(vals)
