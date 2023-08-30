from data.group_data import GroupData
from fw.api.api_base import ApiBase
from data.settings import Settings
from fw.fw_base import FWBase

from fw.api.users.api_users import ApiUsers
from fw.api.users.api_actions_in_users import ApiActionsInUsers
from fw.api.authorization.api_authorization import ApiAuthorization
from fw.api.authorization.api_actions_in_authorization import ApiActionsInAuthorization


class ApplicationManager:

    settings = Settings()
    group_data = GroupData()

    def __init__(self):
        self.fw_base = FWBase(self)
        self.api_base = ApiBase(self)

        self.api_users = ApiUsers(self)
        self.api_actions_in_users = ApiActionsInUsers(self)

        self.api_authorization = ApiAuthorization(self)
        self.api_actions_in_authorization = ApiActionsInAuthorization(self)