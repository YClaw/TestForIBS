from Test.api_tests.api_base import ApiBase


class TestAuthorization(ApiBase):

    email = "eve.holt@reqres.in"

    'Регистрация'
    def test_register(self):
        # Определяем пароль
        password = 'pistol'
        # Регистрируемся
        self.manager.api_actions_in_authorization.register_user(self.email, password)
        # Проверяем статус ответа
        assert self.manager.group_data.response.status_code == 200

    'Регистрация без пароля'
    def test_register_without_password(self):
        # Определяем email
        email = 'sydney@fife'
        # Регистрируемся без пароля
        result = self.manager.api_actions_in_authorization.register_user(email)
        # Проверяем ошибку и статус ответа
        assert result['error'] == 'Missing password'
        assert self.manager.group_data.response.status_code == 400

    'Авторизация'
    def test_login(self):
        # Определяем пароль
        password = 'cityslicka'
        # Авторизуемся
        self.manager.api_actions_in_authorization.login(self.email, password)
        # Проверяем статус ответа
        assert self.manager.group_data.response.status_code == 200

    'Авторизация без пароля'
    def test_login_without_password(self):
        # Определяем email
        email = 'peter@klaven'
        # Авторизуемся без пароля
        result = self.manager.api_actions_in_authorization.login(self.email)
        # Проверяем ошибку и статус ответа
        assert result['error'] == 'Missing password'
        assert self.manager.group_data.response.status_code == 400