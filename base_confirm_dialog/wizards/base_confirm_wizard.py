# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ConfirmEventsWizard(models.TransientModel):
    _name = 'base.confirm.wizard'

    message = fields.Char(string='Message', readonly=True)

    xml_id_action = fields.Char(string='XML ID Action', readonly=True)

    method = fields.Char(string='Method', readonly=True)

    @api.multi
    def yes(self):
        """
        This method calls method validate_record, if no one exception is
        raised, them calls passed method with method_parameters in the context
        (if it was passed), if any return is received through method and the
        xml_id_action field was assigned, then the action is returned with
        generated_records(return value of method, generally ids from related
        model of the returned action)
        :return:
        """
        rec_wiz = self.env[self.env.context.get('active_model')].browse(
            [self.env.context.get('active_id')])

        method_parameters = self.env.context.get('method_parameters') or {}
        generated_records = getattr(rec_wiz, self.method)(**method_parameters)

        if self.xml_id_action and generated_records:
            res = self.env['ir.actions.act_window'].for_xml_id(
                *self.xml_id_action.split('.'))

            res['domain'] = [('id', 'in', generated_records)]

            return res

    @api.multi
    def no(self):
        return False

