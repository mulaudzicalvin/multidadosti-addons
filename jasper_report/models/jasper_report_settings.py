# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
#
# Based in module 'base_external_dbsource'
#

import logging
import psycopg2
from odoo import models, fields, api, _
from odoo.exceptions import Warning as UserError
import odoo.tools as tools

_logger = logging.getLogger(__name__)


CONNECTORS = [('postgres', 'PostgreSQL')]


class JasperReportDBSource(models.Model):

    _name = "jasper.report.db.source"
    _description = 'External Database Sources'

    name = fields.Char('Data Source Name', required=True, size=64)
    db_name = fields.Char('Database Name',
                          default=lambda self: self.env.cr.dbname)
    user_field = fields.Char('User')
    host = fields.Char('Host', default='localhost')
    port = fields.Char('Port', default='5432')
    password = fields.Char('Password', size=40)
    connector = fields.Selection(CONNECTORS, 'Connector', required=True,
                                 default='postgres',
                                 help="If a connector is missing from the\
                                      list, check the server log to confirm\
                                      that the required components were\
                                      detected.")

    @api.multi
    def conn_open(self):
        """The connection is open here."""

        self.ensure_one()
        # Get db source record
        # Build the full connection string

        if self.connector == 'postgres':
            conn_str = "dbname='{0}' " \
                       "user='{1}' " \
                       "host='{2}' " \
                       "port='{3}' " \
                       "password=%s".format(self.db_name,
                                            self.user_field,
                                            self.host,
                                            self.port)

            conn = psycopg2.connect(conn_str % self.password)

        return conn

    @api.multi
    def connection_test(self):
        """Test of connection."""
        self.ensure_one()
        conn = False
        try:
            conn = self.conn_open()
        except Exception as e:
            raise UserError(_("Connection test failed: \
                    Here is what we got instead:\n %s") % tools.ustr(e))
        finally:
            if conn:
                conn.close()

        raise UserError(_("Connection test succeeded: \
                          Everything seems properly set up!"))
