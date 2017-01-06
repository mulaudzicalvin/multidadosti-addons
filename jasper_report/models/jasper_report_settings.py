# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html
#
# Based in module 'base_external_dbsource'
#

# import os
import logging
import psycopg2
from odoo import models, fields, api, _
from odoo.exceptions import Warning as UserError
import odoo.tools as tools

_logger = logging.getLogger(__name__)

# CONNECTORS = []

# try:
#     import sqlalchemy
#     CONNECTORS.append(('sqlite', 'SQLite'))
#     try:
#         import pymssql
#         CONNECTORS.append(('mssql', 'Microsoft SQL Server'))
#         assert pymssql
#     except (ImportError, AssertionError):
#         _logger.info('MS SQL Server not available. Please install "pymssql"\
#                       python package.')
#     try:
#         import MySQLdb
#         CONNECTORS.append(('mysql', 'MySQL'))
#         assert MySQLdb
#     except (ImportError, AssertionError):
#         _logger.info('MySQL not available. Please install "mysqldb"\
#                      python package.')
# except:
#     _logger.info('SQL Alchemy not available. Please install "slqalchemy"\
#                  python package.')
# try:
#     import pyodbc
#     CONNECTORS.append(('pyodbc', 'ODBC'))
# except:
#     _logger.info('ODBC libraries not available. Please install "unixodbc"\
#                  and "python-pyodbc" packages.')
#
# try:
#     import cx_Oracle
#     CONNECTORS.append(('cx_Oracle', 'Oracle'))
# except:
#     _logger.info('Oracle libraries not available. Please install "cx_Oracle"\
#                  python package.')
#
# try:
#     import fdb
#     CONNECTORS.append(('fdb', 'Firebird'))
# except:
#     _logger.info('Firebird libraries not available. Please install "fdb"\
#                  python package.')

CONNECTORS = [('postgres', 'PostgreSQL')]


class JasperReportDBSource(models.Model):
    _name = "jasper.report.db.source"
    _description = 'External Database Sources'

    name = fields.Char('Data Source Name', required=True, size=64)
    db_name = fields.Char('Database Name',
                          default=lambda self: self.env.cr.dbname)
    user_field = fields.Char('User')
    host = fields.Char('Host')
    port = fields.Char('Port')
    password = fields.Char('Password', size=40)
    connector = fields.Selection(CONNECTORS, 'Connector', required=True,
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
            # conn_str = self.conn_string
            # if self.password:
            #     if '%s' not in self.conn_string:
            #         conn_str += ';PWD=%s'
            #     else:
            #
            # conn_str += conn_str % self.password

            # elif self.connector == 'postgres':
            conn = psycopg2.connect(conn_str % self.password)

        return conn

    # @api.multi
    # def execute(self, sqlquery, sqlparams=None, metadata=False,
    #             context=None):
    #     """Executes SQL and returns a list of rows.
    #
    #         "sqlparams" can be a dict of values, that can be referenced in
    #         the SQL statement using "%(key)s" or, in the case of Oracle,
    #         ":key".
    #         Example:
    #             sqlquery = "select * from mytable where city = %(city)s and
    #                         date > %(dt)s"
    #             params   = {'city': 'Lisbon',
    #                         'dt': datetime.datetime(2000, 12, 31)}
    #
    #         If metadata=True, it will instead return a dict containing the
    #         rows list and the columns list, in the format:
    #             { 'cols': [ 'col_a', 'col_b', ...]
    #             , 'rows': [ (a0, b0, ...), (a1, b1, ...), ...] }
    #     """
    #
    #     rows, cols = list(), list()
    #     for obj in self:
    #         conn = obj.conn_open()
    #         if obj.connector in ["sqlite", "mysql", "mssql"]:
    #             # using sqlalchemy
    #             cur = conn.execute(sqlquery, sqlparams)
    #             if metadata:
    #                 cols = cur.keys()
    #             rows = [r for r in cur]
    #
    #         elif obj.connector in ["fdb"]:
    #             # using other db connectors
    #             cur = conn.cursor()
    #             for key in sqlparams:
    #                 sqlquery = sqlquery.replace('%%(%s)s' % key,
    #                                             str(sqlparams[key]))
    #
    #             cur.execute(sqlquery)
    #             rows = cur.fetchall()
    #         else:
    #             # using other db connectors
    #             cur = conn.cursor()
    #             cur.execute(sqlquery, sqlparams)
    #             if metadata:
    #                 cols = [d[0] for d in cur.description]
    #             rows = cur.fetchall()
    #         conn.close()
    #     if metadata:
    #         return{'cols': cols, 'rows': rows}
    #     else:
    #         return rows

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
