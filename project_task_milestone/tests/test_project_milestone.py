# -*- coding: utf-8 -*-


from odoo.tests.common import TransactionCase


class TestProjectMilestone(TransactionCase):

    def setUp(self):
        super(TestProjectMilestone, self).setUp()

        values = {
            'name': 'Milestone Test',
        }

        self.milestone = self.env['project.milestone'].create(values)

    def test__compute_task_count(self):
        # Verificamos o funcionamento do calculo da quantidade de tarefas
        self.milestone._compute_task_count()
        self.assertEqual(self.milestone.task_count, 0)

        # Adicionamos duas tarefas para o milestone e calculamos novamente
        # a quantidade de tarefas
        tasks = self.env.ref('project.project_task_15')
        tasks |= self.env.ref('project.project_task_16')

        self.milestone.project_task_ids = [(6, 0, tasks.ids)]

        self.milestone._compute_task_count()
        self.assertEqual(self.milestone.task_count, 2)

    def action_close_milestone(self):
        # Fecha a milestone. Utilizado quando a campanha é encerrada.
        self.assertEqual(self.milestone.state, 'open')
        self.milestone.close_milestone()
        self.assertEqual(self.milestone.state, 'close')

    def action_reopen_milestone(self):
        # Inicialmente fechamos a milestone
        self.milestone.state.close_milestone()

        # Agora verificamos se a milestone foi aberta
        self.milestone.state.reopen_milestone()
        self.assertEqual(self.milestone.state, 'open')
