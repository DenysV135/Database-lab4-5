from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.episode import Episode

class EpisodeDAO(GeneralDAO):
    def __init__(self):
        super().__init__(Episode)
