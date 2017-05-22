# -*- coding: utf-8 -*-

import functools
import imghdr
import odoo
from odoo import http
from odoo.http import request
from odoo.modules import get_resource_path
from cStringIO import StringIO

db_monodb = http.db_monodb


class Binary(http.Controller):

    @http.route([
        '/web/binary/login_logo',
        '/logo',
        '/logo.png',
    ], type='http', auth="none", cors="*")
    def login_logo(self, dbname=None, **kw):
        imgname = 'logo'
        imgext = '.png'
        placeholder = functools.partial(get_resource_path,
                                        'web_custom_login_page', 'static',
                                        'src', 'img')
        uid = None
        if request.session.db:
            dbname = request.session.db
            uid = request.session.uid
        elif dbname is None:
            dbname = db_monodb()

        if not uid:
            uid = odoo.SUPERUSER_ID

        if not dbname:
            response = http.send_file(placeholder(imgname + imgext))
        else:
            try:
                # create an empty registry
                registry = odoo.modules.registry.Registry(dbname)
                with registry.cursor() as cr:
                    company = int(kw['company']) if kw and kw.get(
                        'company') else False
                    if company:
                        cr.execute("""SELECT logo_web, write_date
                                        FROM res_company
                                       WHERE id = %s
                                   """, (company,))
                    else:
                        cr.execute("""SELECT c.logo_web, c.write_date
                                        FROM res_users u
                                   LEFT JOIN res_company c
                                          ON c.id = u.company_id
                                       WHERE u.id = %s
                                   """, (uid,))
                    row = cr.fetchone()
                    companies = request.env['res.company'].search([])
                    if row and row[0] and len(companies) == 1:
                        image_base64 = str(row[0]).decode('base64')
                        image_data = StringIO(image_base64)
                        imgext = '.' + (imghdr.what(None, h=image_base64) or
                                        'png')
                        response = http.send_file(image_data,
                                                  filename=imgname + imgext,
                                                  mtime=row[1])
                    else:
                        response = http.send_file(
                            placeholder('nologinimage.png'))
            except Exception:
                response = http.send_file(placeholder(imgname + imgext))

        return response
