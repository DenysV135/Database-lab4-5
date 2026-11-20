from flask import Blueprint
from my_project.auth.controller.actor_award_controller import ActorAwardController

actor_award_bp = Blueprint('actor_award', __name__, url_prefix='/api/actor-awards')
actor_award_controller = ActorAwardController()

@actor_award_bp.route('', methods=['GET'])
def get_all(): return actor_award_controller.find_all()

@actor_award_bp.route('/<int:item_id>', methods=['GET'])
def get_by_id(item_id): return actor_award_controller.find_by_id(item_id)

@actor_award_bp.route('', methods=['POST'])
def create(): return actor_award_controller.create()

@actor_award_bp.route('/<int:item_id>', methods=['PUT'])
def update(item_id): return actor_award_controller.update(item_id)

@actor_award_bp.route('/<int:item_id>', methods=['DELETE'])
def delete(item_id): return actor_award_controller.delete(item_id)
