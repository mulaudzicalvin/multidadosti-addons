# -*- coding: utf-8 -*-

from odoo import api, models, _


class ProjectProject(models.Model):

    _inherit = 'project.project'

    @api.multi
    def attachment_tree_view(self):
        self.ensure_one()
        domain = [
            '|',
            '|',
            '&', ('res_model', '=', 'project.project'),
            ('res_id', 'in', self.ids),
            '&', ('res_model', '=', 'calendar.event'),
            ('res_id', 'in', self.calendar_event_ids.ids),
            '&', ('res_model', '=', 'project.task'),
            ('res_id', 'in', self.task_ids.ids)]
        return {
            'name': _('Attachments'),
            'domain': domain,
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'kanban,tree,form',
            'view_type': 'form',
            'help': _('''<p class="oe_view_nocontent_create"> Documents are
            attached to the tasks and issues of your project.</p><p> Send
            messages or log internal notes with attachments to link documents
            to your project.</p>'''),
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d}" %
                       (self._name, self.id)
        }

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
