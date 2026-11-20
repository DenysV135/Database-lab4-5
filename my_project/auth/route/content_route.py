from flask import Blueprint
from my_project.auth.controller.content_controller import ContentController

content_bp = Blueprint('content', __name__, url_prefix='/api/content')
content_controller = ContentController()

@content_bp.route('', methods=['GET'])
def get_all(): return content_controller.find_all()

@content_bp.route('/<int:item_id>', methods=['GET'])
def get_by_id(item_id): return content_controller.find_by_id(item_id)

@content_bp.route('', methods=['POST'])
def create(): return content_controller.create()

@content_bp.route('/<int:item_id>', methods=['PUT'])
def update(item_id): return content_controller.update(item_id)

@content_bp.route('/<int:item_id>', methods=['DELETE'])
def delete(item_id): return content_controller.delete(item_id)

@content_bp.route('/<int:item_id>/actors', methods=['GET'])
def get_content_actors(item_id): return content_controller.get_actors_for_content(item_id)
