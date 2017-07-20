# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    partner_ids = fields.Many2many(comodel_name='res.partner',
                                   related='project_id.partner_ids',
                                   string='Related Partners')

    @api.constrains('user_id')
    def _check_task(self):
        msg = 'Tarefa: ' + self.name + u' atribuída a você.'
        post_vars = {
            'subject': 'Notification',
            'body':  msg,
            'partner_ids': [(4, self.user_id.partner_id.id)],
        }
        self.env['mail.thread'].message_post(
            type="notification", subtype="mt_comment", **post_vars)
