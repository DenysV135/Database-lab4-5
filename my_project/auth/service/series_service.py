from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao.series_dao import SeriesDAO

class SeriesService(GeneralService):
    def __init__(self):
        super().__init__(SeriesDAO())
