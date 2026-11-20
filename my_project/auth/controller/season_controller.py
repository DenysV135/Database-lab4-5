from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.season_service import SeasonService
from my_project.auth.domain.season import Season

class SeasonController(GeneralController):
    def __init__(self):
        super().__init__(SeasonService(), Season)
