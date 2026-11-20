from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.series import Series

class SeriesDAO(GeneralDAO):
    def __init__(self):
        super().__init__(Series)
