# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase


class TestProjectMilestone(TransactionCase):

    def setUp(self):
        super(TestProjectMilestone, self).setUp()

        values = {
            'name': 'Milestone Test',
        }

        self.milestone = self.env['project.milestone'].create(values)

    def test__compute_issue_count(self):
        # Verificamos o funcionamento do calculo da quantidade de tarefas
        self.milestone._compute_issue_count()
        self.assertEqual(self.milestone.issue_count, 0)

        # Adicionamos duas tarefas para o milestone e calculamos novamente
        # a quantidade de tarefas
        issues = self.env.ref('project_issue.crm_case_problemloadingpage0')
        issues |= self.env.ref('project_issue.crm_case_pagenotfound0')

        self.milestone.project_issue_ids = [(6, 0, issues.ids)]

        self.milestone._compute_issue_count()
        self.assertEqual(self.milestone.issue_count, 2)
