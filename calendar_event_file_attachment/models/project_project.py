# -*- coding: utf-8 -*-

from odoo import api, models


class ProjectProject(models.Model):

    _inherit = 'project.project'

    @api.multi
    def attachment_tree_view(self):
        self.ensure_one()
        action = super(ProjectProject, self).attachment_tree_view()
        action['domain'] = [
            '|',
            '|',
            '&', ('res_model', '=', 'project.project'),
            ('res_id', 'in', self.ids),
            '&', ('res_model', '=', 'calendar.event'),
            ('res_id', 'in', self.calendar_event_ids.ids),
            '&', ('res_model', '=', 'project.task'),
            ('res_id', 'in', self.task_ids.ids)]
        return action

    def _compute_attached_docs_count(self):
        ir_attachment = self.env['ir.attachment']
        for project in self:
            project.doc_count = ir_attachment.search_count([
                '|',
                '|',
                '&',
                ('res_model', '=', 'project.project'),
                ('res_id', '=', project.id),
                '&',
                ('res_model', '=', 'calendar.event'),
                ('res_id', 'in', project.calendar_event_ids.ids),
                '&',
                ('res_model', '=', 'project.task'),
                ('res_id', 'in', project.task_ids.ids)
            ])
