from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.actor_award import ActorAward

class ActorAwardDAO(GeneralDAO):
    def __init__(self):
        super().__init__(ActorAward)
