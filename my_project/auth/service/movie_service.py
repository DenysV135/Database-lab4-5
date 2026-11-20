from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao.movie_dao import MovieDAO

class MovieService(GeneralService):
    def __init__(self):
        super().__init__(MovieDAO())
