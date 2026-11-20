from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.trivia import Trivia

class TriviaDAO(GeneralDAO):
    def __init__(self):
        super().__init__(Trivia)
