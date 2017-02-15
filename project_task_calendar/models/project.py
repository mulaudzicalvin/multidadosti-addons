# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models


class ProjectProject(models.Model):

    _inherit = 'project.project'

    partner_ids = fields.Many2many(comodel_name='res.partner',
                                   string='Related Partners')

    calendar_event_ids = fields.One2many(comodel_name='calendar.event',
                                         inverse_name='project_id',
                                         string='Calendar Events')

    bring_default_task_type = fields.Boolean(
        string='Get default stages',
        help='Add to this project, all stage defined like default')

    allow_meetings = fields.Boolean('Allow Meetings', default=True)

    meeting_number = fields.Integer(compute='_get_meeting_number',
                                    string='Number of Meetings')

    @api.model
    def create(self, values):
        values['partner_ids'] = [(4, values['partner_id'])]
        res = super(ProjectProject, self).create(values)

        if values.get('bring_default_task_type'):
            task_types = self.env['project.task.type'].search([(
                'is_default', '=', 'True')])
            for rec in task_types:
                rec.project_ids = [(4, res.id)]

        return res

    @api.multi
    def write(self, values):
        if 'partner_id' in values:
            values['partner_ids'] = [(4, values['partner_id'])]
        return super(ProjectProject, self).write(values)

    @api.multi
    def _get_meeting_number(self):
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

    meeting_number = fields.Integer(compute='_get_meeting_number',
                                    string='Number of Meetings')

    @api.multi
    def _get_meeting_number(self):
        for record in self:
            cal_events = record.calendar_event_ids.filtered(
                lambda r: r.meeting_state == 'open')
            record.meeting_number = len(cal_events)

    @api.multi
    def action_make_meeting(self):
        """ This opens Meeting's calendar view to schedule meeting on current applicant
            @return: Dictionary value for created Meeting view
        """
        self.ensure_one()

        task_owner_id = self.env['res.users'].browse(self.env.uid)
        partners = task_owner_id.partner_id | self.user_id.partner_id

        category = self.env.ref('calendar.categ_meet1')

        res = self.env['ir.actions.act_window'].for_xml_id(
            'calendar', 'action_calendar_event')

        res['context'] = {
            'search_default_partner_ids': task_owner_id.name,
            'search_default_task_id': self.id,
            'default_partner_id': self.partner_id.id,
            'default_partner_ids': partners.ids,
            'default_user_id': self.env.uid,
            'default_name': self.name,
            'default_project_id': self.project_id.id,
            'default_task_id': self.id,
            'default_categ_ids': category and [category.id] or False,
        }

        return res


class ProjectTaskType(models.Model):

    _inherit = 'project.task.type'

    is_default = fields.Boolean(string='Default',
                                help='Allows assignment of the current stage '
                                     'to new projects that will be created.')

    _sql_constraints = [('project_task_type_name_uniq', 'unique (name)',
                         'Already stage with same name!')]

