from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.movie_service import MovieService
from my_project.auth.domain.movie import Movie

class MovieController(GeneralController):
    def __init__(self):
        super().__init__(MovieService(), Movie)
