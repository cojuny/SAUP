from flask import Flask
from app.routes.common_route import common 
from app.routes.kafka_route import kafka 
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(common)
    app.register_blueprint(kafka)

    return app
