from flask import Blueprint
from my_project.auth.controller.trivia_controller import TriviaController

trivia_bp = Blueprint('trivia', __name__, url_prefix='/api/trivia')
trivia_controller = TriviaController()

@trivia_bp.route('', methods=['GET'])
def get_all(): return trivia_controller.find_all()

@trivia_bp.route('/<int:item_id>', methods=['GET'])
def get_by_id(item_id): return trivia_controller.find_by_id(item_id)

@trivia_bp.route('', methods=['POST'])
def create(): return trivia_controller.create()

@trivia_bp.route('/<int:item_id>', methods=['PUT'])
def update(item_id): return trivia_controller.update(item_id)

@trivia_bp.route('/<int:item_id>', methods=['DELETE'])
def delete(item_id): return trivia_controller.delete(item_id)
