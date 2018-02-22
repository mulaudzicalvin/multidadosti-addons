from odoo import fields, models


class ProjectTask(models.Model):

    _inherit = 'project.task'

    calendar_event_ids = fields.One2many(comodel_name='calendar.event',
                                         inverse_name='task_id',
                                         readonly=True,
                                         string='Calendar Events')
