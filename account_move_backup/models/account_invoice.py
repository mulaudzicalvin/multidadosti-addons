# -*- coding: utf-8 -*-

from odoo import api, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def action_invoice_cancel_paid(self):
        backup_move = self._prepare_dict_to_create_backup_record(self.move_id)
        if backup_move:
            self.env['account.move.backup'].create(backup_move)
        return super(AccountInvoice, self).action_invoice_cancel_paid()

    def _prepare_dict_to_create_backup_record(self, rec, backup_dict=None):
        """
        :param rec: Record that will be used to examine type of each field
                       to adjust it in case of relational type.
        :param backup_dict: Base dict containing each field of 'rec' object.
        :param limit_lvl: How deep the function is called recursively(like
                          levels in graphs).
        :return: backup_dict with fields of relational type readjusted.
        """
        if rec:
            backup_dict = rec.read()[0] if backup_dict is None else backup_dict

            date_fields_to_avoid = ['create_date', 'write_date', 'id',
                                    'create_uid', 'write_uid']

            for field in date_fields_to_avoid:
                if field in backup_dict:
                    backup_dict.pop(field)

            dic_fields_to_avoid = dict(rec._field_inverses._map,
                                       **rec._field_computed)

            for field in dic_fields_to_avoid:
                if (rec._fields[field.name].type != 'one2many' and
                            field.name in backup_dict):
                    backup_dict.pop(field.name)
                    continue

            readjusted_dict = dict(backup_dict)

            for field in backup_dict:
                if not rec[field]:
                    readjusted_dict.pop(field)
                elif rec._fields[field].type == 'many2one' and rec[field]:
                    readjusted_dict[field] = rec[field].id

                elif rec._fields[field].type == 'many2many' and rec[field]:
                    many2many_lines = []
                    for line in rec[field]:
                        many2many_lines.insert(0, line.id)
                    readjusted_dict[field] = [(6, 0, many2many_lines)]

                elif rec._fields[field].type == 'one2many' and rec[field]:
                    readjusted_dict[field] = []
                    for line in rec[field]:
                        line_dic = self._prepare_dict_to_create_backup_record(
                            line)
                        readjusted_dict[field].insert(0, (0, 0, line_dic))

            return readjusted_dict
