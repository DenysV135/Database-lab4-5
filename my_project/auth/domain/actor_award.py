from my_project import db

class ActorAward(db.Model):
    __tablename__ = 'actor_awards'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    award_name = db.Column(db.String(100), nullable=False)
    award_year = db.Column(db.Integer, nullable=False)
    actor_id = db.Column(db.Integer, nullable=False)

    @staticmethod
    def put_into_dto(item):
        return {
            "id": item.id,
            "award_name": item.award_name,
            "award_year": item.award_year,
            "actor_id": item.actor_id
        }

    @staticmethod
    def put_into_entity(data):
        return ActorAward(
            award_name=data.get('award_name'),
            award_year=data.get('award_year'),
            actor_id=data.get('actor_id')
        )
