from flask import Blueprint
from my_project.auth.controller.procedure_controller import ProcedureController

procedure_bp = Blueprint('procedure', __name__, url_prefix='/api/procedures')
procedure_controller = ProcedureController()


@procedure_bp.route('/insert-actor', methods=['POST'])
def insert_actor():
    return procedure_controller.insert_actor()


@procedure_bp.route('/link-actor-content', methods=['POST'])
def link_actor_content():
    return procedure_controller.link_actor_content()


@procedure_bp.route('/insert-10-subscriptions', methods=['POST'])
def insert_10_subscriptions():
    return procedure_controller.insert_10_noname_subscriptions()


@procedure_bp.route('/avg-rating', methods=['GET'])
def avg_rating():
    return procedure_controller.get_avg_review_rating()


@procedure_bp.route('/split-actors', methods=['POST'])
def split_actors():
    return procedure_controller.split_actors_cursor()