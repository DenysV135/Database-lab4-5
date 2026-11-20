from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao.episode_dao import EpisodeDAO

class EpisodeService(GeneralService):
    def __init__(self):
        super().__init__(EpisodeDAO())
