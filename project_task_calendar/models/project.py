# -*- coding: utf-8 -*-
# Project Task Calendar
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import pytz

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    calendar_event_ids = fields.One2many(comodel_name="calendar.event",
                                         inverse_name="project_id",
                                         string=u"Eventos de Calendário")

    bring_default_task_type = fields.Boolean(
        string=u"Trazer estágios padronizados",
        help=u"Atribui ao atual projeto, todos"
             u" os estágios que foram criados "
             u"com status Padrão")

    @api.model
    def create(self, vals):
        res = super(ProjectProject, self).create(vals)

        if vals.get('bring_default_task_type'):
            task_types = self.env['project.task.type'].search([(
                'is_default', '=', 'True')])
            for rec in task_types:
                rec.project_ids = [(4, res.id)]

        return res


class MultiProjectTaskType(models.Model):

    _inherit = 'project.task.type'

    is_default = fields.Boolean(string=u"Padrão",
                                help=u"Permite Atribuição do atual estágio"
                                     u" a novos projetos que serão criados")

    _sql_constraints = [("project_task_type_name_uniq",
                         "unique (name)",
                        u"Já existe um estágio com esse mesmo nome!")]


class ProjectTask(models.Model):
    _inherit = 'project.task'

    start = fields.Datetime('Start', required=False,
                            help="Start date of an event, without "
                                 "time for full days events")
    stop = fields.Datetime('Stop', required=False,
                           help="Stop date of an event, without time "
                                "for full days events")

    allday = fields.Boolean('All Day', default=False)
    start_date = fields.Date('Start Date', compute='_compute_dates',
                             inverse='_inverse_dates', store=True,
                             track_visibility='onchange')
    start_datetime = fields.Datetime('Start DateTime',
                                     compute='_compute_dates',
                                     inverse='_inverse_dates', store=True,
                                     track_visibility='onchange')
    stop_date = fields.Date('End Date', compute='_compute_dates',
                            inverse='_inverse_dates', store=True,
                            track_visibility='onchange')
    stop_datetime = fields.Datetime('End Datetime', compute='_compute_dates',
                                    inverse='_inverse_dates', store=True,
                                    track_visibility='onchange')
    duration = fields.Float(u'Duração')

    @api.multi
    @api.depends('allday', 'start', 'stop')
    def _compute_dates(self):
        """ Adapt the value of start_date(time)/stop_date(time) according
        to start/stop fields and all day. Also, compute the duration for not
        all day meeting ; otherwise the duration is set to zero, since the
        meeting last all the day.
        """
        for meeting in self:
            if meeting.allday:
                meeting.start_date = meeting.start
                meeting.start_datetime = False
                meeting.stop_date = meeting.stop
                meeting.stop_datetime = False
                meeting.date_start = meeting.start
                meeting.date_deadline = meeting.stop

                meeting.duration = 0.0
            else:
                meeting.start_date = False
                meeting.start_datetime = meeting.start
                meeting.stop_date = False
                meeting.stop_datetime = meeting.stop
                meeting.date_start = False
                meeting.date_deadline = False

                meeting.duration = self._get_duration(meeting.start,
                                                      meeting.stop)

    @api.multi
    def _inverse_dates(self):
        for meeting in self:
            if meeting.allday:
                tz = pytz.timezone(
                    self.env.user.tz) if self.env.user.tz else pytz.utc

                enddate = fields.Datetime.from_string(meeting.stop_date)
                enddate = tz.localize(enddate)
                enddate = enddate.replace(hour=18)
                enddate = enddate.astimezone(pytz.utc)
                meeting.stop = fields.Datetime.to_string(enddate)
                meeting.date_deadline = meeting.stop

                startdate = fields.Datetime.from_string(meeting.start_date)
                startdate = tz.localize(startdate)  # Add "+hh:mm" timezone
                startdate = startdate.replace(hour=8)  # Set 8 AM in localtime
                startdate = startdate.astimezone(pytz.utc)  # Convert to UTC
                meeting.start = fields.Datetime.to_string(startdate)
                meeting.date_start = meeting.start
            else:
                meeting.start = meeting.start_datetime
                meeting.stop = meeting.stop_datetime
                meeting.date_start = meeting.start
                meeting.date_deadline = meeting.stop

    def _get_duration(self, start, stop):
        """ Get the duration value between the 2 given dates. """
        if start and stop:
            diff = fields.Datetime.from_string(stop) - \
                fields.Datetime.from_string(start)
            if diff:
                duration = float(diff.days) * 24 + (float(diff.seconds) / 3600)
                return round(duration, 2)
            return 0.0
