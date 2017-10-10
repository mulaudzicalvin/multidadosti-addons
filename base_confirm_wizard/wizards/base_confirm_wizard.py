# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import AccessError
from odoo.tools.translate import _


class BaseConfirmWizard(models.TransientModel):
    _name = 'base.confirm.wizard'

    message = fields.Char(string='Message', readonly=True)

    xml_id_action = fields.Char(string='XML ID Action', readonly=True)

    method = fields.Char(string='Method', readonly=True)

    def validate_method(self, rec_wiz):
        """
        This method validates if method exists in active_model and if there is
        method parameters in context, if so, them verifies if parameters
        matches with related parameters in method.
        """
        if hasattr(rec_wiz, self.method):
            ctx_method_parameters = (self.env.context.get('method_parameters')
                                     or {})
            method = getattr(rec_wiz, self.method)
            method_parameters = method.func_code.co_varnames
            undefined_parameters = [var for var in ctx_method_parameters
                                    if var not in method_parameters]

            if ctx_method_parameters and undefined_parameters:
                raise AccessError(_(
                    'The following method parameters are not implemented:\n-%s')
                    % '\n-'.join(undefined_parameters))
        else:
            raise AccessError(_(
                'The following method is not implemented:\n-%s') % self.method)

    def validate_xml_action(self):
        """
        This method validates if xml_id_action is valid(in other words, if the
        module is installed/exists and if action exists in module).
        """
        module_name, act_name = self.xml_id_action.split('.')
        module_recs = self.env['ir.module.module'].search([('name', '=',
                                                            module_name)])
        if module_recs:
            action = self.env['ir.model.data'].search(
                ['&', ('module', '=', module_name), ('name', '=', act_name)])
            if not action:
                raise AccessError(
                    'The following action is not implemented in %s module:'
                    '\n-%s' % (module_name, act_name))
        else:
            raise AccessError(
                _('The following module is not installed:\n-%s') % module_name)

    def validate_record(self):
        """
        This method calls methods of method validation and XML action
        validation if a xml_id_action was passed if no one exception is raised,
        then return active_ids records.
        :return: active_id record
        """

        rec_wiz = self.env[self.env.context.get('active_model')].browse(
            self.env.context.get('active_ids'))
        self.validate_method(rec_wiz)

        if self.xml_id_action:
            self.validate_xml_action()

        return rec_wiz

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
        rec_wiz = self.validate_record()
        method_parameters = self.env.context.get('method_parameters') or {}
        generated_records = getattr(rec_wiz, self.method)(**method_parameters)

        if self.xml_id_action and generated_records:
            res = self.env['ir.actions.act_window'].for_xml_id(
                *self.xml_id_action.split('.'))

            res['domain'] = [('id', 'in', generated_records)]
            if 'action_context' in self.env.context:
                res['context'] = self.env.context.get('action_context')

            return res

    @api.multi
    def no(self):
        return False

