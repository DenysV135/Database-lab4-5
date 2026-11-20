from my_project import db

class ContentActors(db.Model):
    __tablename__ = 'content_actors'

    actors_id = db.Column(db.Integer, db.ForeignKey('actors.id'), primary_key=True)
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), primary_key=True)
    role_name = db.Column(db.String(45), nullable=False)

    actor = db.relationship('Actor', back_populates='contents')
    content = db.relationship('Content', back_populates='actors')

    @staticmethod
    def put_into_dto(item):
        return {
            "actors_id": item.actors_id,
            "actor_name": item.actor.name if item.actor else None,
            "content_id": item.content_id,
            "content_title": item.content.title if item.content else None,
            "role_name": item.role_name
        }

    @staticmethod
    def put_into_entity(data):
        return ContentActors(
            actors_id=data.get('actors_id'),
            content_id=data.get('content_id'),
            role_name=data.get('role_name')
        )
