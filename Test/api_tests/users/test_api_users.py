import pytest

from Test.api_tests.api_base import ApiBase


class TestUsers(ApiBase):

    pages = [1, 2]

    'Получение всех пользователей на странице'
    @pytest.mark.parametrize('page', pages)
    def test_get_all_users_on_page(self, page):
        # Получаем список пользоваетелей
        result = self.manager.api_users.get_list_users(page)
        # Проверяем страницу и статус ответа
        assert result['page'] == page
        assert self.manager.group_data.response.status_code == 200

    users_data = list(range(1, 13))

    'Получение конкретного пользователя'
    @pytest.mark.parametrize('user_id', users_data)
    def test_get_single_user(self, user_id):
        # Получаем пользователя по id
        result = self.manager.api_users.get_single_user(user_id)
        # Проверяем id пользователя и статус ответа
        assert result['data']['id'] == user_id
        assert self.manager.group_data.response.status_code == 200

    'Конкретный кользователь не найден'
    def test_single_user_not_found(self):
        # Получаем пользователя по id
        self.manager.api_users.get_single_user(23)
        # Проверяем статус ответа
        assert self.manager.group_data.response.status_code == 404

    'Получение всех пользователей с задержкой'
    def test_get_all_users_with_delay(self):
        delay = 3
        # Получаем пользователей с задержкой
        self.manager.api_users.get_list_users_with_delay(delay)
        # Проверяем статус ответа
        assert self.manager.group_data.response.status_code == 200
