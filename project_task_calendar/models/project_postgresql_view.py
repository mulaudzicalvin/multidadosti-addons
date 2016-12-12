# -*- coding: utf-8 -*-
# # Project Task Calendar
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models, tools


class NewModule(models.Model):

    _name = 'union.project.task.calendar.event'
    _description = 'SQL view to union project.task and calendar.event tables'
    _auto = False

    name = fields.Char(readonly=True)
    start = fields.Datetime('Start', readonly=True,
                            help="Start date of an event, without "
                                 "time for full days events")
    stop = fields.Datetime('Stop', readonly=True,
                           help="Stop date of an event, without time "
                                "for full days events")

    all_day = fields.Boolean('All Day', readonly=True)
    start_date = fields.Date('Start Date', readonly=True)
    start_datetime = fields.Datetime('Start DateTime', readonly=True)
    stop_date = fields.Date('End Date', readonly=True)
    stop_datetime = fields.Datetime('End Datetime', readonly=True)
    duration = fields.Float('Duration', readonly=True)

    location = fields.Char('Location', readonly=True)
    recurrent = fields.Boolean('Recurrent', readonly=True)
    user_id = fields.Many2one('res.users', readonly=True)
    project_id = fields.Many2one('project.project', readonly=True)
    origin = fields.Char('Origin', readonly=True)

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
                     ce.allday as all_day,
                     ce.duration as duration,
                     ce.location as location,
                     ce.recurrency as recurrent,
                     ce.user_id as user_id,
                     ce.project_id as project_id
        """
        return select_str


    def _select_project_task(self):
        select_str = """
                     SELECT
                     ce.id as id,
                     ce.name as name,
                     'Project Task' as origin,
                     ce.start as start,
                     ce.stop as stop,
                     ce.start_date as start_date,
                     ce.start_datetime as start_datetime,
                     ce.stop_date as stop_date,
                     ce.stop_datetime as stop_datetime,
                     ce.all_day as all_day,
                     ce.duration as duration,
                     '' as location,
                     false as recurrent,
                     ce.user_id as user_id,
                     ce.project_id as project_id
        """
        return select_str

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE view %s as
              %s
              FROM calendar_event ce
              WHERE t.active = 'true'
              UNION
              %s
              FROM project_task pt
              WHERE t.active = 'true'
        """ % (self._table, self._select_calendar_event(),
               self._select_project_task()))
