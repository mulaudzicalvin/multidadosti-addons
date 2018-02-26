from odoo import api, models, fields
from odoo.tools.translate import _


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    def _attachment_ids_domain(self):
        return [('res_model', '=', self._name)]

    attachment_ids = fields.One2many(comodel_name='ir.attachment',
                                     inverse_name='res_id',
                                     domain=_attachment_ids_domain,
                                     auto_join=True,
                                     string='Attachments')

    doc_count = fields.Integer(compute='_compute_attached_docs_count',
                               string="Number of documents attached")

    @api.multi
    def attachment_tree_view(self):
        self.ensure_one()
        domain = [
            '&',
            ('res_model', '=', 'calendar.event'), ('res_id', '=', self.id)
        ]
        return {
            'name': _('Attachments'),
            'domain': domain,
            'res_model': 'ir.attachment',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'kanban,tree,form',
            'view_type': 'form',
            'help': _('''<p class="oe_view_nocontent_create">
                        Documents are attached to the tasks and issues of your
                        project.</p><p> Send messages or log internal notes
                        with attachments to link documents to your project.
                    </p>'''),
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d}" %
                       (self._name, self.id)
        }

    def _compute_attached_docs_count(self):
        ir_attachment = self.env['ir.attachment']
        for meeting in self:
            meeting.doc_count = ir_attachment.search_count([
                '&',
                ('res_model', '=', 'calendar.event'),
                ('res_id', '=', meeting.id)
            ])
