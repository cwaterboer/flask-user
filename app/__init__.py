from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the app
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(Config)

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes
from app import routes

# If you have models, import them as well
from app import models
