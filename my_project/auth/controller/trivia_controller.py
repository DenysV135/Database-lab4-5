from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.trivia_service import TriviaService
from my_project.auth.domain.trivia import Trivia

class TriviaController(GeneralController):
    def __init__(self):
        super().__init__(TriviaService(), Trivia)
