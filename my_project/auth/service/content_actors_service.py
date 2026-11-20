from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao.content_actors_dao import ContentActorsDAO

class ContentActorsService(GeneralService):
    def __init__(self):
        super().__init__(ContentActorsDAO())

    def find_by_ids(self, actors_id, content_id):
        return self.dao.find_by_ids(actors_id, content_id)

    def update_by_ids(self, actors_id, content_id, data):
        return self.dao.update_by_ids(actors_id, content_id, data)

    def delete_by_ids(self, actors_id, content_id):
        return self.dao.delete_by_ids(actors_id, content_id)
