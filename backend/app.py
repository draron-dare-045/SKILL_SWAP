# backend/app.py
from flask import Flask, cli
from flask_cors import CORS
from config import Config
from extensions import db, bcrypt, jwt, ma, migrate
from models import User # Ensure models are imported
import click

# Import blueprints
from routes.auth_routes import auth_bp
from routes.skill_routes import skill_bp
from routes.user_routes import user_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    CORS(app, origins="https://skill-swap-silk-eight.vercel.app") # Allow all origins for simplicity

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(skill_bp, url_prefix='/api/skills')
    app.register_blueprint(user_bp, url_prefix='/api/users')
    
    # Add a CLI command to seed the database
    @app.cli.command("seed")
    def seed_db():
        """Creates a default admin user."""
        from seed import seed_admin
        seed_admin()
        print("Admin user seeded.")

    return app