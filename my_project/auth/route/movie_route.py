from flask import Blueprint
from my_project.auth.controller.movie_controller import MovieController

movie_bp = Blueprint('movie', __name__, url_prefix='/api/movies')
movie_controller = MovieController()

@movie_bp.route('', methods=['GET'])
def get_all(): return movie_controller.find_all()

@movie_bp.route('/<int:item_id>', methods=['GET'])
def get_by_id(item_id): return movie_controller.find_by_id(item_id)

@movie_bp.route('', methods=['POST'])
def create(): return movie_controller.create()

@movie_bp.route('/<int:item_id>', methods=['PUT'])
def update(item_id): return movie_controller.update(item_id)

@movie_bp.route('/<int:item_id>', methods=['DELETE'])
def delete(item_id): return movie_controller.delete(item_id)
