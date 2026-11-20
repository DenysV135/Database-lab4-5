from flask import Blueprint
from my_project.auth.controller.series_controller import SeriesController

series_bp = Blueprint('series', __name__, url_prefix='/api/series')
series_controller = SeriesController()

@series_bp.route('', methods=['GET'])
def get_all(): return series_controller.find_all()

@series_bp.route('/<int:item_id>', methods=['GET'])
def get_by_id(item_id): return series_controller.find_by_id(item_id)

@series_bp.route('', methods=['POST'])
def create(): return series_controller.create()

@series_bp.route('/<int:item_id>', methods=['PUT'])
def update(item_id): return series_controller.update(item_id)

@series_bp.route('/<int:item_id>', methods=['DELETE'])
def delete(item_id): return series_controller.delete(item_id)
