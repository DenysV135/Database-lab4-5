from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.user import User

class UserDAO(GeneralDAO):
    def __init__(self):
        super().__init__(User)
