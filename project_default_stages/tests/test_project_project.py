from odoo.tests.common import TransactionCase


class TestProjectProject(TransactionCase):

    def setUp(self):
        super(TestProjectProject, self).setUp()

        self.project_values = {
            'name': 'Projeto Teste',
            'label_tasks': 'Tasks',
            'partner_id': self.env.ref('base.res_partner_4').id,
            'bring_default_task_type': True,
        }

        self.project_stage_0 = self.env.ref('project.project_stage_data_0')
        self.project_stage_2 = self.env.ref('project.project_stage_data_2')

    def test_create_with_default_task(self):

        # Adicionamos todas os estagios de tarefas como False
        for task_type in self.env['project.task.type'].search([]):
            task_type.case_default = False

        # Definimos os estagios New e Advanced como estagios default do
        # projeto, logo elas serao adicionadas quando criamos um projeto
        # e marcamos o checkbox para trazer estagios padrao
        self.project_stage_0.case_default = True
        self.project_stage_2.case_default = True

        # Definimos que o projeto deve utilizar estagios default
        self.project_values['bring_default_task_type'] = True

        project = self.env['project.project'].create(self.project_values)

        # Verificamos se os estagios do projeto sao apenas os dois estagios
        # que definimos como True
        self.assertEqual(len(project.type_ids), 2)

        self.assertIn(self.project_stage_0.id, project.type_ids.ids)
        self.assertIn(self.project_stage_2.id, project.type_ids.ids)

    def test_create_with_default_task(self):

        # Definimos que o projeto nao deve utilizar estagios default
        self.project_values['bring_default_task_type'] = False

        project = self.env['project.project'].create(self.project_values)

        # Verificamos se os estagios do projeto sao apenas os dois estagios
        # que definimos como True
        self.assertEqual(len(project.type_ids), 0)

        self.assertNotIn(self.project_stage_0.id, project.type_ids.ids)
        self.assertNotIn(self.project_stage_2.id, project.type_ids.ids)
