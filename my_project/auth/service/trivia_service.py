from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao.trivia_dao import TriviaDAO

class TriviaService(GeneralService):
    def __init__(self):
        super().__init__(TriviaDAO())
