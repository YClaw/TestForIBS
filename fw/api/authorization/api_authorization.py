from fw.api.api_base import ApiBase


class ApiAuthorization(ApiBase):

    'Регистрация'
    def post_register(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'register', body, params)

    'Авторизация'
    def post_login(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'login', body, params)
