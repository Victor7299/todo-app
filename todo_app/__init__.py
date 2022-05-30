from flask import Flask
#Extensions
from .extensions import db
# Blueprints
from .core.routes import core

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    @app.before_first_request
    def create_db():
        db.create_all()

    db.init_app(app)

    app.register_blueprint(core)

    return app