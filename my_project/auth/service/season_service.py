from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao.season_dao import SeasonDAO

class SeasonService(GeneralService):
    def __init__(self):
        super().__init__(SeasonDAO())
