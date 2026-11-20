from my_project import db


class ProcedureDAO:
    def _call_procedure(self, proc_name, args=()):
        conn = db.engine.raw_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.callproc(proc_name, args)
            results = []
            for result in cursor.stored_results():
                results.extend(result.fetchall())
            conn.commit()
            return results
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()

    def insert_actor(self, name, birthday):
        return self._call_procedure('sp_insert_actor', (name, birthday))

    def link_actor_content(self, actor_name, content_title, role_name):
        return self._call_procedure('sp_link_actor_content', (actor_name, content_title, role_name))

    def insert_10_noname_subscriptions(self, start_num):
        return self._call_procedure('sp_insert_10_noname_subscriptions', (start_num,))

    def get_avg_review_rating(self):
        return self._call_procedure('sp_get_avg_review_rating')

    def split_actors_cursor(self):
        return self._call_procedure('sp_split_actors_cursor')