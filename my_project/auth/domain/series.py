from my_project import db

class Series(db.Model):
    __tablename__ = 'series'

    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), primary_key=True)
    seasons = db.relationship('Season', backref='series', lazy='dynamic')

    @staticmethod
    def put_into_dto(item):
        return {
            "content_id": item.content_id,
            "seasons": [
                {"id": s.id, "number": s.number, "name": s.name}
                for s in item.seasons
            ]
        }

    @staticmethod
    def put_into_entity(data):
        return Series(
            content_id=data.get('content_id')
        )
