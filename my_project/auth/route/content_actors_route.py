from flask import Blueprint
from my_project.auth.controller.content_actors_controller import ContentActorsController

content_actors_bp = Blueprint('content_actors', __name__, url_prefix='/api/content-actors')
content_actors_controller = ContentActorsController()

@content_actors_bp.route('', methods=['GET'])
def get_all(): return content_actors_controller.find_all()

@content_actors_bp.route('/<int:actors_id>/<int:content_id>', methods=['GET'])
def get_by_ids(actors_id, content_id): return content_actors_controller.find_by_ids(actors_id, content_id)

@content_actors_bp.route('', methods=['POST'])
def create(): return content_actors_controller.create()

@content_actors_bp.route('/<int:actors_id>/<int:content_id>', methods=['PUT'])
def update_by_ids(actors_id, content_id): return content_actors_controller.update_by_ids(actors_id, content_id)

@content_actors_bp.route('/<int:actors_id>/<int:content_id>', methods=['DELETE'])
def delete_by_ids(actors_id, content_id): return content_actors_controller.delete_by_ids(actors_id, content_id)
