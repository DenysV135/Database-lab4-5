from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.series_service import SeriesService
from my_project.auth.domain.series import Series

class SeriesController(GeneralController):
    def __init__(self):
        super().__init__(SeriesService(), Series)
