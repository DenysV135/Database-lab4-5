from my_project import db

class Season(db.Model):
    __tablename__ = 'season'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    series_id = db.Column(db.Integer, db.ForeignKey('series.content_id'), nullable=False)

    episodes = db.relationship('Episode', backref='season', lazy='dynamic')

    @staticmethod
    def put_into_dto(item):
        return {
            "id": item.id,
            "number": item.number,
            "name": item.name,
            "series_id": item.series_id,
            "episodes": [
                {"id": e.id, "number": e.number, "name": e.name, "duration_mins": e.duration_mins}
                for e in item.episodes
            ]
        }

    @staticmethod
    def put_into_entity(data):
        return Season(
            number=data.get('number'),
            name=data.get('name'),
            series_id=data.get('series_id')
        )
