# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models, _


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
        Attachment = self.env['ir.attachment']
        for project in self:
            project.doc_count = Attachment.search_count([
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

    # partner_ids = fields.Many2many(comodel_name='res.partner',
    #                                string='Related Partners')

    calendar_event_ids = fields.One2many(comodel_name='calendar.event',
                                         inverse_name='project_id',
                                         string='Calendar Events')

    # bring_default_task_type = fields.Boolean(
    #     string='Get default stages',
    #     deafult=True,
    #     help='Add to this project, all stage defined like default')

    # allow_meetings = fields.Boolean('Allow Meetings', default=True)

    meeting_number = fields.Integer(compute='_compute_meeting_number',
                                    string='Number of Meetings')

    # project_classification = fields.Selection(
    #     string="Classification",
    #     selection=([('0', 'Without Classification'),
    #                 ('1', 'Terrible'),
    #                 ('2', 'Bad'),
    #                 ('3', 'Good'),
    #                 ('4', 'Great'),
    #                 ('5', 'Excellent')]), default='0')

    # planned_time = fields.Float(string="Planned Time")

    # project_tags_ids = fields.Many2many(comodel_name='project.tags',
    #                                     string='Tags')

    # @api.model
    # def create(self, values):
    #     values['partner_ids'] = [(4, values['partner_id'])]
    #     res = super(ProjectProject, self).create(values)
    #
    #     if values.get('bring_default_task_type'):
    #
    #         task_types = self.env['project.task.type'].search([(
    #             'is_default', '=', 'True')])
    #         for rec in task_types:
    #             rec.project_ids = [(4, res.id)]
    #
    #     return res

    # @api.multi
    # def write(self, values):
    #     if 'partner_id' in values:
    #         values['partner_ids'] = [(4, values['partner_id'])]
    #     return super(ProjectProject, self).write(values)

    @api.multi
    def _compute_meeting_number(self):
        for record in self:
            cal_events = record.calendar_event_ids.filtered(
                lambda r: r.meeting_state == 'open')
            record.meeting_number = len(cal_events)


class ProjectTask(models.Model):

    _inherit = 'project.task'

    calendar_event_ids = fields.One2many(comodel_name='calendar.event',
                                         inverse_name='task_id',
                                         readonly=True,
                                         string='Calendar Events')

    meeting_number = fields.Integer(compute='_compute_meeting_number',
                                    string='Number of Meetings')

    @api.multi
    def _compute_meeting_number(self):
        for record in self:
            cal_events = record.calendar_event_ids.filtered(
                lambda r: r.meeting_state == 'open')
            record.meeting_number = len(cal_events)

    # @api.multi
    # def action_make_meeting(self):
    #     """ This opens Meeting's calendar view to schedule meeting on
    #     current applicant
    #         @return: Dictionary value for created Meeting view
    #     """
    #     self.ensure_one()
    #
    #     task_owner_id = self.env['res.users'].browse(self.env.uid)
    #     partners = task_owner_id.partner_id | self.user_id.partner_id
    #
    #     category = self.env.ref('calendar.categ_meet1')
    #
    #     res = self.env['ir.actions.act_window'].for_xml_id(
    #         'calendar', 'action_calendar_event')
    #
    #     res['context'] = {
    #         'search_default_partner_ids': task_owner_id.name,
    #         'search_default_task_id': self.id,
    #         'default_partner_id': self.partner_id.id,
    #         'default_partner_ids': partners.ids,
    #         'default_user_id': self.env.uid,
    #         'default_name': self.name,
    #         'default_project_id': self.project_id.id,
    #         'default_task_id': self.id,
    #         'default_categ_ids': category and [category.id] or False,
    #     }
    #
    #     return res


# class ProjectTaskType(models.Model):
#
#     _inherit = 'project.task.type'
#
#     is_default = fields.Boolean(string='Default',
#                                 help='Allows assignment of the current
# stage to new projects that will be created.')
#
#     _sql_constraints = [('project_task_type_name_uniq', 'unique (name)',
#                          'Already stage with same name!')]


# class ProjectProjectTags(models.Model):
#     """ Tags of project's tasks (or issues) """
#     _name = "project.project.tags"
#     _description = "Project Tags"
#
#     name = fields.Char(required=True)
#     color = fields.Integer(string='Color Index')
#
#     _sql_constraints = [
#         ('name_uniq', 'unique (name)', "Tag name already exists !"),
#     ]
