from my_project import db

class Episode(db.Model):
    __tablename__ = 'episode'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    duration_mins = db.Column(db.Integer, nullable=False)
    season_id = db.Column(db.Integer, db.ForeignKey('season.id'), nullable=False)

    @staticmethod
    def put_into_dto(item):
        return {
            "id": item.id,
            "name": item.name,
            "number": item.number,
            "duration_mins": item.duration_mins,
            "season_id": item.season_id
        }

    @staticmethod
    def put_into_entity(data):
        return Episode(
            name=data.get('name'),
            number=data.get('number'),
            duration_mins=data.get('duration_mins'),
            season_id=data.get('season_id')
        )
