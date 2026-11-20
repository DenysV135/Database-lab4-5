from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao.content_dao import ContentDAO

class ContentService(GeneralService):
    def __init__(self):
        super().__init__(ContentDAO())
