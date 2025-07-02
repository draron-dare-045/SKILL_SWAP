# backend/config.py
import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    # Get the database URL from the environment.
    # Fall back to a local SQLite database if DATABASE_URL is not set.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///dev.db'

    # The psycopg2 library expects "postgresql" but many providers use "postgres"
    # This line automatically fixes the URI if necessary.
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'a-very-secret-key-for-dev'