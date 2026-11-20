from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.content import Content

class ContentDAO(GeneralDAO):
    def __init__(self):
        super().__init__(Content)
