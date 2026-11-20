from flask import jsonify, request
from my_project import db
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.actor_award_service import ActorAwardService
from my_project.auth.domain.actor_award import ActorAward

class ActorAwardController(GeneralController):
    def __init__(self):
        super().__init__(ActorAwardService(), ActorAward)

    def create(self):
        try:
            return super().create()
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    def update(self, item_id):
        try:
            return super().update(item_id)
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
