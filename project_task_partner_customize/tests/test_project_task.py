# -*- coding: utf-8 -*-

import mock

from odoo.tests.common import TransactionCase


class TestProjectTask(TransactionCase):

    def setUp(self):
        super(TestProjectTask, self).setUp()

    @mock.patch('odoo.addons.project_task_partner_customize.models.project_task.ProjectTask._send_message')  # noqa: E501
    def test_create(self, mock_send_message):

        tasks_before = self.env['project.task'].search([])

        # Verificamos se a tarefa criada ja nao estava na lista
        task = self.env['project.task'].create({'name': 'Test Task'})
        self.assertNotIn(task, tasks_before)

        # Verificamos se a tarefa criada esta na nova lista de tarefas
        tasks_now = self.env['project.task'].search([])
        self.assertIn(task, tasks_now)

        # Verificamos se o metodo _send_message foi chamado uma vez
        self.assertEqual(1, mock_send_message.call_count)
        self.assertEqual(2, len(mock_send_message.call_args))

    @mock.patch('odoo.addons.project_task_partner_customize.models.project_task.ProjectTask._send_message')  # noqa: E501
    def test_write(self, mock_send_message):
        task = self.env.ref('project.project_task_15')

        # Verificamos se o nome da tarefa nao foi alterado
        self.assertEqual('User Interface design', task.name)

        ret = task.write({'name': 'Test Task'})

        # Verificamos se o metodo write foi executado corretamente
        self.assertEqual('Test Task', task.name)
        self.assertTrue(ret)

        # Verificamos se o metodo _send_message foi chamado uma vez e se a
        # quantidade de parametro esta correta
        self.assertEqual(1, mock_send_message.call_count)
        self.assertEqual(2, len(mock_send_message.call_args))

    @mock.patch('odoo.addons.mail.models.mail_thread.MailThread.message_post')  # noqa: E501
    def test__send_message_success(self, mock_message_post):
        task = self.env.ref('project.project_task_15')

        ret = task._send_message({'user_id': task.user_id.id}, task)
        self.assertTrue(ret)

        post_vars = {
            'subject': u'Nova tarefa atribuída a você',
            'body': u'Tarefa: %s atribuída a você.' % task.name,
            'partner_ids': [(4, task.user_id.partner_id.id)],
            'message_type': 'notification',
            'subtype': 'mt_comment',
        }

        mock_message_post.assert_called_once_with(**post_vars)

    def test__send_message_fail(self):
        task = self.env['project.task'].create({'name': 'Test Task'})

        # O método create do project.task chama o metodo message_post
        # logo, devemos deixa-lo fora do mock, para que essa chamada nao seja
        # contabilizado e influencie no teste

        with mock.patch('odoo.addons.mail.models.mail_thread.MailThread.message_post') as mock_message_post:  # noqa: E501

            ret = task._send_message({}, task)
            self.assertFalse(ret)
            self.assertEqual(0, mock_message_post.call_count)

            ret = task._send_message({'user_id': False}, task)
            self.assertFalse(ret)
            self.assertEqual(0, mock_message_post.call_count)
