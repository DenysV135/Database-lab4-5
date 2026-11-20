from flask import Blueprint
from my_project.auth.controller.season_controller import SeasonController

season_bp = Blueprint('season', __name__, url_prefix='/api/seasons')
season_controller = SeasonController()

@season_bp.route('', methods=['GET'])
def get_all(): return season_controller.find_all()

@season_bp.route('/<int:item_id>', methods=['GET'])
def get_by_id(item_id): return season_controller.find_by_id(item_id)

@season_bp.route('', methods=['POST'])
def create(): return season_controller.create()

@season_bp.route('/<int:item_id>', methods=['PUT'])
def update(item_id): return season_controller.update(item_id)

@season_bp.route('/<int:item_id>', methods=['DELETE'])
def delete(item_id): return season_controller.delete(item_id)
