import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# Initialize Flask app
app = Flask(__name__)

# Configure app
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

with app.app_context():
    try:
        # Test database connection
        db.engine.connect()
        logging.info("Database connection successful")
    except Exception as e:
        logging.error(f"Database connection failed: {str(e)}")
        raise

# Log successful initialization
logging.info("Flask app and SQLAlchemy initialized successfully")
