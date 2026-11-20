from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao.actor_award_dao import ActorAwardDAO

class ActorAwardService(GeneralService):
    def __init__(self):
        super().__init__(ActorAwardDAO())
