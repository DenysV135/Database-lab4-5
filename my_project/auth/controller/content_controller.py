from flask import jsonify, abort
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service.content_service import ContentService
from my_project.auth.domain.content import Content

class ContentController(GeneralController):
    def __init__(self):
        super().__init__(ContentService(), Content)

    def get_actors_for_content(self, content_id):
        content = self.service.find_by_id(content_id)
        if not content:
            abort(404, description="Контент не знайдено")
        result = [
            {
                "actor_id": link.actors_id,
                "actor_name": link.actor.name if link.actor else None,
                "birthday": str(link.actor.birthday) if link.actor and link.actor.birthday else None,
                "role_name": link.role_name
            }
            for link in content.actors
        ]
        return jsonify(result), 200
