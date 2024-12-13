import logging
import os
from app import app, db

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# Import models first
from models import User, Memo
# Then import routes which use the models
import routes

def init_db():
    """Initialize the database and create tables"""
    try:
        with app.app_context():
            logging.info("Creating database tables...")
            db.create_all()
            logging.info("Database tables created successfully")
    except Exception as e:
        logging.error(f"Failed to create database tables: {str(e)}")
        raise

if __name__ == '__main__':
    try:
        # Initialize database
        init_db()
        
        # Start Flask application
        logging.info("Starting Flask application...")
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as e:
        logging.error(f"Error starting application: {str(e)}")
        raise
