from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.movie import Movie

class MovieDAO(GeneralDAO):
    def __init__(self):
        super().__init__(Movie)
