# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    partner_ids = fields.Many2many(comodel_name='res.partner',
                                   related='project_id.partner_ids',
                                   string='Related Partners')

    # Atributo default foi sobrescrito para evitar que o usuario fosse
    # atribuido automaticamente por engano
    user_id = fields.Many2one(default=False)

    @api.model
    def create(self, values):
        project_task = super(ProjectTask, self).create(values)

        if 'user_id' in values and values.get('user_id'):
            self._send_message()

        return project_task

    @api.multi
    def write(self, values):
        ret = super(ProjectTask, self).write(values)

        if 'user_id' in values and values.get('user_id'):
            self._send_message()

        return ret

    def _send_message(self):

        post_vars = {
            'subject': u'Nova tarefa atribuída a você',
            'body': u'Tarefa: %s atribuída a você.' % self.name,
            'partner_ids': [(4, self.user_id.partner_id.id)],
            'message_type': 'notification',
            'subtype': 'mt_comment',
        }

        self.env['mail.thread'].message_post(**post_vars)
