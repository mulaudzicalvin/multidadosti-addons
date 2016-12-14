# -*- coding: utf-8 -*-
# Project Task Calendar
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models, tools


class UnionProjectTaskCalendarEvent(models.Model):

    _name = 'union.project.task.calendar.event'
    _description = 'SQL view to union project.task and calendar.event tables'
    _auto = False

    name = fields.Char(readonly=True)
    origin = fields.Char('Origin', readonly=True)
    start = fields.Datetime('Start', readonly=True,
                            help="Start date of an event, without "
                                 "time for full days events")
    stop = fields.Datetime('Stop', readonly=True,
                           help="Stop date of an event, without time "
                                "for full days events")

    allday = fields.Boolean('All Day', readonly=True)
    start_date = fields.Date('Start Date', readonly=True)
    start_datetime = fields.Datetime('Start DateTime', readonly=True)
    stop_date = fields.Date('End Date', readonly=True)
    stop_datetime = fields.Datetime('End Datetime', readonly=True)
    duration = fields.Float(u'Duração', readonly=True)
    user_id = fields.Many2one('res.users', readonly=True)
    project_id = fields.Many2one('project.project', string='Project',
                                 readonly=True)
    project_task_id = fields.Many2one('project.task', string='Project task',
                                      readonly=True)
    calendar_event_id = fields.Many2one('calendar.event',
                                        string='Calendar Event',
                                        readonly=True)

    def _select_calendar_event(self):
        select_str = """
                SELECT
                     ce.id as id,
                     ce.name as name,
                     'Calendar Event' as origin,
                     ce.start as start,
                     ce.stop as stop,
                     ce.start_date as start_date,
                     ce.start_datetime as start_datetime,
                     ce.stop_date as stop_date,
                     ce.stop_datetime as stop_datetime,
                     ce.allday as allday,
                     ce.duration as duration,
                     ce.user_id as user_id,
                     ce.project_id as project_id,
                     NULL as project_task_id,
                     ce.id as calendar_event_id
        """
        return select_str

    def _select_project_task(self):
        select_str = """
                     SELECT
                     pt.id as id,
                     pt.name as name,
                     'Project Task' as origin,
                     pt.start as start,
                     pt.stop as stop,
                     pt.start_date as start_date,
                     pt.start_datetime as start_datetime,
                     pt.stop_date as stop_date,
                     pt.stop_datetime as stop_datetime,
                     pt.allday as allday,
                     pt.duration as duration,
                     pt.user_id as user_id,
                     pt.project_id as project_id,
                     pt.id as project_task_id,
                     NULL as calendar_event_id
        """
        return select_str

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("CREATE view %s as %s "
                         "FROM calendar_event ce "
                         "WHERE ce.active = 'true' "
                         "UNION "
                         "%s FROM project_task pt "
                         "WHERE pt.active = 'true'",
                         (self._table,
                          self._select_calendar_event(),
                          self._select_project_task()))
