from odoo.tests import TransactionCase


class TestCalendarEvent(TransactionCase):

    def setUp(self):
        super(TestCalendarEvent, self).setUp()

        # self.project_values = {
        #     'name': 'Projeto Teste',
        #     'use_tasks': True,
        #     'label_tasks': 'Tasks',
        #     'partner_id': self.env.ref('base.res_partner_4').id,
        #     'bring_default_task_type': True,
        # }

        self.project = self.env.ref('project.project_project_3')
        self.task = self.env.ref('project.project_task_13')
        self.ce = self.env.ref('calendar.calendar_event_2')

    def test__compute_record_name(self):

        self.assertFalse(self.ce.project_name)
        self.assertFalse(self.ce.task_name)

        # testa calendar event sem projeto e tarefa
        self.ce._compute_record_name()

        self.assertEqual(self.ce.project_name, '')
        self.assertEqual(self.ce.task_name, '')

        # Adicionamos um projeto para o evento de calendario
        self.ce.project_id = self.project.id

        self.ce._compute_record_name()

        self.assertEqual(self.ce.project_name, ' * ' + self.project.name)
        self.assertEqual(self.ce.task_name, '')

        # Finalmente, adicionamos uma tarefa para o evento de calendario
        self.ce.task_id = self.task.id

        self.ce._compute_record_name()

        self.assertEqual(self.ce.project_name, ' * ' + self.project.name)
        self.assertEqual(self.ce.task_name, ' * ' + self.task.name)
