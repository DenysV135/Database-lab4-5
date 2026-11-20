from my_project import db

class Movie(db.Model):
    __tablename__ = 'movie'

    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), primary_key=True)
    duration_mins = db.Column(db.Integer, nullable=False)

    @staticmethod
    def put_into_dto(item):
        return {
            "content_id": item.content_id,
            "duration_mins": item.duration_mins
        }

    @staticmethod
    def put_into_entity(data):
        return Movie(
            content_id=data.get('content_id'),
            duration_mins=data.get('duration_mins')
        )
