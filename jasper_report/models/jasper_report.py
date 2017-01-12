# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# @author Michell Stuttgart <michellstut@gmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

import os
from pyjasper import jasperpy
import tempfile


class JasperReport:

    def __init__(self):
        self.jasper_client = jasperpy.JasperPy()

    def compile(self,  template, output_file=False, redirect_output=True):
        self.jasper_client.compile(template, output_file=output_file,
                                   redirect_output=redirect_output)

    def process(self, template, output_format, parameters, db_parameters):

        with tempfile.NamedTemporaryFile(suffix='.jrxml') as file_temp:
            file_temp.write(template.decode('base64'))
            file_temp.flush()

            # db_param = {
            #     'username': self.username,
            #     'database': self.database,
            #     'host': self.host,
            #     'port': self.port,
            #     'password': self.password,
            #     'driver': self.driver,
            # }

            self.jasper_client.process(file_temp.name,
                                       output_file=tempfile.gettempdir(),
                                       format_list=[output_format],
                                       parameters=parameters,
                                       db_connection=db_parameters)

            output = file_temp.name.replace('.jrxml', '.%s' % output_format)

            with open(output, 'rb') as file_bin:
                data = file_bin.read().encode('base64')

            os.unlink(output)

        return data

    def get_parameters(self, template):

        with tempfile.NamedTemporaryFile(suffix='.jrxml') as file_temp:
            file_temp.write(template.decode('base64'))
            file_temp.flush()

            output = self.jasper_client.list_parameters(file_temp.name)

        return output
