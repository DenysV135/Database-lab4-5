from my_project import db
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.content_actors import ContentActors

class ContentActorsDAO(GeneralDAO):
    def __init__(self):
        super().__init__(ContentActors)

    def find_by_ids(self, actors_id, content_id):
        return db.session.query(ContentActors).filter_by(
            actors_id=actors_id, content_id=content_id
        ).first()

    def update_by_ids(self, actors_id, content_id, data):
        item = self.find_by_ids(actors_id, content_id)
        if item:
            if 'role_name' in data:
                item.role_name = data['role_name']
            db.session.commit()
        return item

    def delete_by_ids(self, actors_id, content_id):
        item = self.find_by_ids(actors_id, content_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return True
        return False
