from flask import jsonify, request, abort
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.content_actors_service import ContentActorsService
from my_project.auth.domain.content_actors import ContentActors

class ContentActorsController(GeneralController):
    def __init__(self):
        super().__init__(ContentActorsService(), ContentActors)

    def find_by_ids(self, actors_id, content_id):
        item = self.service.find_by_ids(actors_id, content_id)
        if item:
            return jsonify(ContentActors.put_into_dto(item)), 200
        abort(404, description="Зв'язок не знайдено")

    def update_by_ids(self, actors_id, content_id):
        data = request.get_json()
        if not data:
            abort(400, description="Очікується JSON")
        updated = self.service.update_by_ids(actors_id, content_id, data)
        if updated:
            return jsonify(ContentActors.put_into_dto(updated)), 200
        abort(404, description="Зв'язок не знайдено")

    def delete_by_ids(self, actors_id, content_id):
        if self.service.delete_by_ids(actors_id, content_id):
            return '', 204
        abort(404, description="Зв'язок не знайдено")
