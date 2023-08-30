from fw.api.api_base import ApiBase


class ApiActionsInAuthorization(ApiBase):

    'Регистрация пользователя'
    def register_user(self, email=None, password=None):
        body = {
            'email': email,
            'password': password
        }

        return self.manager.api_authorization.post_register(body)

    'Авторизация'
    def login(self, email=None, password=None):
        body = {
            'email': email,
            'password': password
        }

        return self.manager.api_authorization.post_login(body)