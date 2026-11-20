from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.season import Season

class SeasonDAO(GeneralDAO):
    def __init__(self):
        super().__init__(Season)
