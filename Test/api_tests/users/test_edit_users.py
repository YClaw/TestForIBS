from Test.api_tests.api_base import ApiBase


class TestEditUsers(ApiBase):

    name = 'morpheus'

    'Создание пользователя'
    def test_create_user(self):
        # Определяем данные пользователя
        job = 'leader'
        # Формируем тело
        body = {
            'name': self.name,
            'job': job
        }
        # Создаем пользователя
        result = self.manager.api_users.post_create_user(body)
        # Сравниваем имя и работу созданного пользоваетеля
        assert result['name'] == self.name
        assert result['job'] == job
        # Сравниваем статус ответа
        assert self.manager.group_data.response.status_code == 201

    'Редактирование работы пользователя (PUT)'
    def test_edit_users_job_use_put(self):
        user_id = 2
        # Объявляем данные для редактирования
        new_job = 'zion resident'
        # Редактируем работу пользователя
        result = self.manager.api_actions_in_users.edit_user({'Id': user_id, 'Name': self.name, 'Job': new_job})
        # Сравниваем имя и работу отредактированного пользователя
        assert result['name'] == self.name
        assert result['job'] == new_job
        # Сравниваем статус ответа
        assert self.manager.group_data.response.status_code == 200

    'Редактирование работы пользователя'
    def test_edit_users_job_use_patch(self):
        user_id = 2
        # Объявляем данные для редактирования
        new_job = 'zion resident'
        # Редактируем работу пользователя
        result = self.manager.api_actions_in_users.edit_user({'Id': user_id, 'Name': self.name, 'Job': new_job}, request_type='PATCH')
        # Сравниваем имя и работу отредактированного пользователя
        assert result['name'] == self.name
        assert result['job'] == new_job
        # Сравниваем статус ответа
        assert self.manager.group_data.response.status_code == 200

    'Удаление пользователя'
    def test_delete_user(self):
        user_id = 2
        # Удаляем пользователя
        self.manager.api_users.delete_user(user_id)
        # Сравниваем статус
        assert self.manager.group_data.response.status_code == 204