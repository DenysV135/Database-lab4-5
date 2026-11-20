from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.episode_service import EpisodeService
from my_project.auth.domain.episode import Episode

class EpisodeController(GeneralController):
    def __init__(self):
        super().__init__(EpisodeService(), Episode)
