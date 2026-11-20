from flask import Blueprint
from my_project.auth.controller.episode_controller import EpisodeController

episode_bp = Blueprint('episode', __name__, url_prefix='/api/episodes')
episode_controller = EpisodeController()

@episode_bp.route('', methods=['GET'])
def get_all(): return episode_controller.find_all()

@episode_bp.route('/<int:item_id>', methods=['GET'])
def get_by_id(item_id): return episode_controller.find_by_id(item_id)

@episode_bp.route('', methods=['POST'])
def create(): return episode_controller.create()

@episode_bp.route('/<int:item_id>', methods=['PUT'])
def update(item_id): return episode_controller.update(item_id)

@episode_bp.route('/<int:item_id>', methods=['DELETE'])
def delete(item_id): return episode_controller.delete(item_id)
