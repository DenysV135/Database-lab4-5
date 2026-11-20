import os
import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.json.ensure_ascii = False

    base_dir = os.path.abspath(os.path.dirname(__file__))
    yaml_path = os.path.join(base_dir, '..', 'config', 'app.yml')

    with open(yaml_path, 'r') as file:
        config = yaml.safe_load(file)

    db_config = config['db']
    db_url = f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from my_project.auth.route.subscription_route import subscription_bp
        from my_project.auth.route.actor_route import actor_bp
        from my_project.auth.route.age_rating_route import age_rating_bp
        from my_project.auth.route.genre_route import genre_bp
        from my_project.auth.route.user_review_route import user_review_bp
        from my_project.auth.route.user_route import user_bp
        from my_project.auth.route.content_route import content_bp
        from my_project.auth.route.content_actors_route import content_actors_bp
        from my_project.auth.route.movie_route import movie_bp
        from my_project.auth.route.series_route import series_bp
        from my_project.auth.route.season_route import season_bp
        from my_project.auth.route.episode_route import episode_bp
        from my_project.auth.route.trivia_route import trivia_bp
        from my_project.auth.route.actor_award_route import actor_award_bp
        from my_project.auth.route.procedure_route import procedure_bp

        for bp in [
            subscription_bp, actor_bp, age_rating_bp, genre_bp, user_review_bp,
            user_bp, content_bp, content_actors_bp, movie_bp, series_bp,
            season_bp, episode_bp, trivia_bp, actor_award_bp, procedure_bp
        ]:
            app.register_blueprint(bp)

    return app
