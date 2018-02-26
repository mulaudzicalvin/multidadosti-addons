from odoo import api, fields, models


class Partner(models.Model):

    _inherit = "res.partner"

    user_id = fields.Many2one('res.users', compute='_compute_user_id')

    @api.multi
    def _compute_user_id(self):
        for rec in self:
            user = self.env['res.users'].search([('partner_id', '=', rec.id)])
            if user:
                rec.user_id = user.id
                user.image = rec.image
