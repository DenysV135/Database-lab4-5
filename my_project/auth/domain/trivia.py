from my_project import db

class Trivia(db.Model):
    __tablename__ = 'trivia'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(45), nullable=False)
    fact = db.Column(db.Text, nullable=True)
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)

    @staticmethod
    def put_into_dto(item):
        return {
            "id": item.id,
            "title": item.title,
            "fact": item.fact,
            "content_id": item.content_id
        }

    @staticmethod
    def put_into_entity(data):
        return Trivia(
            title=data.get('title'),
            fact=data.get('fact'),
            content_id=data.get('content_id')
        )
