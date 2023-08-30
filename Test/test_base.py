from fw.application_manager import ApplicationManager
from data.settings import Settings

class TestBase:

    manager = ApplicationManager()
    reqres_main_page = Settings.GLOBAL['Reqres']['WEB']['Link']

    def setup_module(self):
        pass

    def setup_class(self):
        pass

    def setup_module(self):
        pass

    def teardown_class(self):
        pass

    def teardown_method(self):
        pass

    def teardown_module(self):
        pass
