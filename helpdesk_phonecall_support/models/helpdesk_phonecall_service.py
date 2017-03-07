# -*- coding: utf-8 -*-

from odoo.exceptions import UserError
from odoo import api, fields, models, _


class HelpDeskPhoneCallService(models.Model):

    _name = 'helpdesk.phonecall.service'
    _rec_name = 'title'

    title = fields.Char(string='Title', compute='_onchange_title')

    description = fields.Text(string='Description')

    start_date_hour = fields.Datetime(string='Start Date',
                                      readonly=True,
                                      default=lambda s: fields.Datetime.now())

    partner_id = fields.Many2one(string='Partner',
                                 required=True,
                                 comodel_name='res.partner')

    project_id = fields.Many2one(string="Project",
                                 required=True,
                                 comodel_name='project.project')

    contact_partner_id = fields.Many2one(string='Contact',
                                         required=True,
                                         comodel_name='res.partner')

    user_id = fields.Many2one('res.users', string='User', readonly=True,
                              default=lambda self: self._uid)

    finish_date_hour = fields.Datetime(string='Finish Date',
                                       readonly=True, )

    phonecall_tag_id = fields.Many2one('helpdesk.phonecall.service.tag',
                                       string='Tags')

    state = fields.Selection(string='State', readonly=True,
                             selection=[
                                 ('open', 'Open'),
                                 ('done', 'Done')
                             ],
                             default='open')

    @api.onchange('start_date_hour', 'partner_id', 'project_id')
    def _onchange_title(self):
        for rec in self:
            rec.title = ''
            rec.title += rec.start_date_hour if rec.start_date_hour else ''
            rec.title += ', ' + rec.partner_id.name if rec.partner_id else ''
            rec.title += ', ' + rec.project_id.name if rec.project_id else ''

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if not self.partner_id.is_company:
            self.contact_partner_id = self.partner_id
        else:
            self.contact_partner_id = False

    @api.multi
    def _action_finish_phonecall(self):
        self.ensure_one()
        if (not self.project_tag_id) or (not self.description):
            raise UserError(_('Please make sure the marker or '
                              'description fields are filled in.'))

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'helpdesk.phonecall.confirm',
            'view_type': 'form',
            'view_mode': 'form',
            'views': [(False, "form")],
            'target': 'new',
        }
