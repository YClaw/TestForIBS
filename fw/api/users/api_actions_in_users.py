from fw.api.api_base import ApiBase


class ApiActionsInUsers(ApiBase):

    'Отредактировать данные пользователя'
    def edit_user(self, data={}, request_type='PUT'):
        json_request = {}

        if "Name" in data:
            json_request['name'] = data['Name']

        if "Job" in data:
            json_request['job'] = data['Job']

        if request_type == 'PUT':
            return self.manager.api_users.put_update_user(data['Id'], json_request)
        elif request_type == 'PATCH':
            return self.manager.api_users.patch_update_user(data['Id'], json_request)
