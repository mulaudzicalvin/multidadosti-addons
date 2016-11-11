# -*- coding: utf-8 -*-
#    Geo localization to Brazil Localization to Odoo
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Michell Stuttgart <m.faria@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def zip_search(self):
        self.ensure_one()
        res = super(ResPartner, self).zip_search()
        self.geo_localize()
        return res
