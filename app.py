from flask import Flask
from extensions import db, migrate
from routes.vacinaroute import vacinaroute
from routes.vacinado_route import vacinadoroute
from routes.vacinador_route import vacinador_route
from routes.aplicacao_route import aplicacaoroute


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(vacinaroute)
    app.register_blueprint(vacinadoroute)
    app.register_blueprint(vacinador_route)
    app.register_blueprint(aplicacaoroute)

    return app


if __name__ == '__main__':
    create_app()
