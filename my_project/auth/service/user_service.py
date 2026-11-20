from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao.user_dao import UserDAO

class UserService(GeneralService):
    def __init__(self):
        super().__init__(UserDAO())
