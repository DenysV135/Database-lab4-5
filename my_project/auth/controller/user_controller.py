from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.user_service import UserService
from my_project.auth.domain.user import User

class UserController(GeneralController):
    def __init__(self):
        super().__init__(UserService(), User)
