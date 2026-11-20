from flask import jsonify, request
from my_project.auth.service.procedure_service import ProcedureService


class ProcedureController:
    def __init__(self):
        self.service = ProcedureService()

    def insert_actor(self):
        data = request.get_json()
        if not data or 'name' not in data or 'birthday' not in data:
            return jsonify({"error": "Потрібно передати name та birthday"}), 400
        try:
            res = self.service.insert_actor(data['name'], data['birthday'])
            return jsonify(res), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def link_actor_content(self):
        data = request.get_json()
        if not data or 'actor_name' not in data or 'content_title' not in data or 'role_name' not in data:
            return jsonify({"error": "Потрібно передати actor_name, content_title та role_name"}), 400
        try:
            res = self.service.link_actor_content(
                data['actor_name'],
                data['content_title'],
                data['role_name']
            )
            return jsonify(res), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def insert_10_noname_subscriptions(self):
        data = request.get_json(silent=True) or {}
        start_num = data.get('start_num', 1)
        try:
            res = self.service.insert_10_noname_subscriptions(int(start_num))
            return jsonify(res), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def get_avg_review_rating(self):
        try:
            res = self.service.get_avg_review_rating()
            return jsonify(res), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def split_actors_cursor(self):
        try:
            res = self.service.split_actors_cursor()
            return jsonify(res), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400