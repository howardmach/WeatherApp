# app/__init__.py
# Initializes the Flask app and sets up the MongoDB connection

from flask import Flask
from flask_pymongo import PyMongo
import os

# Create a PyMongo instance (shared across the app)
mongo = PyMongo()

def create_app():
    """
    Application factory function.
    Configures Flask app and registers blueprints.
    """
    app = Flask(__name__)

    # Set up MongoDB URI from environment variable or default
    app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/weatherapp")

    # Initialize PyMongo with the app
    mongo.init_app(app)

    # Register blueprints (routes)
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app