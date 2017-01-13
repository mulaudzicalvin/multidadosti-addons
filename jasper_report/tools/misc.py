# -*- coding: utf-8 -*-
# Copyright (C) 2017 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

import os

from odoo.tools import config
from odoo.tools.translate import _
from odoo.exceptions import RedirectWarning


def mount_path_jasper(db_name, report_name):
    filestore = config.filestore(db_name)
    report_path = '/'.join([filestore,
                            'jasper_report',
                            str(report_name)])

    if not os.path.exists(report_path):
        try:
            os.makedirs(report_path)
        except OSError:
            raise RedirectWarning(
                _(u'Erro!'),
                _(u"""Verifique as permissões de escrita
                e o caminho da pasta"""))
    return report_path
