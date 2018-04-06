from odoo import api, fields, models


class ProjectTeam(models.Model):

    _name = 'project.team'
    _description = 'Project Team'

    name = fields.Char(required=True)

    lead_id = fields.Many2one(comodel_name='res.users',
                              string='Team Lead',
                              required=True)

    member_ids = fields.Many2many(comodel_name='res.users',
                                  string='Team Members')

    @api.model
    def create(self, values):
        if not values['member_ids']:
            values['member_ids'] = [(4, values['lead_id'])]
        else:
            values['member_ids'][0][2].append(values['lead_id'])

        return super(ProjectTeam, self).create(values)

    @api.multi
    def write(self, values):

        if 'lead_id' not in values and self.lead_id:
            values['lead_id'] = self.lead_id.id

        if 'lead_id' in values:
            if not values.get('member_ids', None):
                values['member_ids'] = [(4, values['lead_id'])]
            else:
                values['member_ids'][0][2].append(values['lead_id'])

        return super(ProjectTeam, self).write(values)
