# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase


class TestProjectProject(TransactionCase):

    def setUp(self):
        super(TestProjectProject, self).setUp()

        self.project = self.env.ref('project.project_project_3')

        self.analytic_default = {
            'name': 'Analytic Line Test',
            'date': '2017-10-02',
            'user_id': self.env.user.id,
            'partner_id': self.project.partner_id.id,
            'company_id': self.env.user.company_id.id,
            'project_id': self.project.id,
        }

    def test__compute_hours_left(self):

        # Testamos com todos os valores como zero
        self.assertFalse(self.project.planned_time)
        self.assertFalse(self.project.hours_left)
        self.assertFalse(self.project.progress)

        self.project._compute_hours_left()

        self.assertFalse(self.project.planned_time)
        self.assertFalse(self.project.hours_left)
        self.assertFalse(self.project.progress)

        # 100 horas em segundos. Testamos apenas com planned_time diferente
        # de zero
        self.project.planned_time = 360000.0

        self.project._compute_hours_left()

        self.assertEqual(self.project.hours_left, 360000.0)
        self.assertFalse(self.project.progress, 0.0)

        # Criamos duas entradas na planilha de horas com total de 3 horas
        # Uma entrada de duracao igual a 1 hora
        self.env['account.analytic.line'].create(
            dict(self.analytic_default.items(),
                 unit_amount=3600.0))

        # Uma entrada de duracao igual a 2 hora
        self.env['account.analytic.line'].create(
            dict(self.analytic_default.items(),
                 unit_amount=7200.0))

        self.project._compute_hours_left()

        total_horas = 3600.0 + 7200.0

        self.assertEqual(self.project.hours_left, 360000.0 - total_horas)
        self.assertEqual(self.project.progress, 100 * total_horas/360000.0)
