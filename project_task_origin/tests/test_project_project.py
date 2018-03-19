# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase


class TestProjectProject(TransactionCase):

    def setUp(self):
        super(TestProjectProject, self).setUp()

        self.project = self.env['project.project'].create({
            'name': 'Project Task Origin Test'
        })

        self.tasks = self.env['project.task'].create({
            'name': '1',
            'project_id': self.project.id,
            'origin': 'feature',
        })

        self.tasks |= self.env['project.task'].create({
            'name': '2',
            'project_id': self.project.id,
            'origin': 'feature'
        })

        self.tasks |= self.env['project.task'].create({
            'name': '3',
            'project_id': self.project.id,
            'origin': 'issue'
        })

    def test__compute_task_origin_count(self):
        self.project._compute_task_origin_count()
        self.assertEqual(self.project.task_origin_feature_count, 2)
        self.assertEqual(self.project.task_origin_issue_count, 1)
