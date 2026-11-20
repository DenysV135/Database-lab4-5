from flask import Blueprint
from my_project.auth.controller.user_controller import UserController

user_bp = Blueprint('user', __name__, url_prefix='/api/users')
user_controller = UserController()

@user_bp.route('', methods=['GET'])
def get_all(): return user_controller.find_all()

@user_bp.route('/<int:item_id>', methods=['GET'])
def get_by_id(item_id): return user_controller.find_by_id(item_id)

@user_bp.route('', methods=['POST'])
def create(): return user_controller.create()

@user_bp.route('/<int:item_id>', methods=['PUT'])
def update(item_id): return user_controller.update(item_id)

@user_bp.route('/<int:item_id>', methods=['DELETE'])
def delete(item_id): return user_controller.delete(item_id)
