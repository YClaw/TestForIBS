from fw.api.api_base import ApiBase


class ApiUsers(ApiBase):

    'Получить список пользователей на странице'
    def get_list_users(self, page, params=None):
        return self.requests_GET(self.get_base_url() + f'users?page={page}', params)


    'Получить конкретного пользователя'
    def get_single_user(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'users/{id}', params)

    'Получить список пользователей с задержкой'
    def get_list_users_with_delay(self, delay, params=None):
        return self.requests_GET(self.get_base_url() + f'users/?delay={delay}', params)

    'Создать пользователя пользователя'
    def post_create_user(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'users', body, params)

    'Отредактировать пользователя (Put)'
    def put_update_user(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'users/{id}', body, params)

    'Отредатировать пользователя (Patch)'
    def patch_update_user(self, id, body, params=None):
        return self.requests_PATCH(self.get_base_url() + f'users/{id}', body, params)

    'Удаление пользователя'
    def delete_user(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'users/{id}', params)
