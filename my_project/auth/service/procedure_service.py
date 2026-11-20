from my_project.auth.dao.procedure_dao import ProcedureDAO


class ProcedureService:
    def __init__(self):
        self.dao = ProcedureDAO()

    def insert_actor(self, name, birthday):
        return self.dao.insert_actor(name, birthday)

    def link_actor_content(self, actor_name, content_title, role_name):
        return self.dao.link_actor_content(actor_name, content_title, role_name)

    def insert_10_noname_subscriptions(self, start_num):
        return self.dao.insert_10_noname_subscriptions(start_num)

    def get_avg_review_rating(self):
        return self.dao.get_avg_review_rating()

    def split_actors_cursor(self):
        return self.dao.split_actors_cursor()