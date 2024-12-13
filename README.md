# Flask Memo Application

A secure web application that allows users to create and manage personal memos. Built with Flask and SQLAlchemy.

## Features

- User Authentication (Register/Login)
- Personal Memo Management
- Automatic Save
- Secure Password Handling
- Database Integration

## Technologies

- Flask
- SQLAlchemy
- Flask-Login
- WTForms
- PostgreSQL

## Setup

1. Click "Run" to start the Flask application
2. The server will run on port 5001
3. Register a new account or login with existing credentials
4. Start creating and managing your memos

## Usage

1. Register/Login to access your personal memo space
2. Write or edit your memo content
3. Changes are automatically saved
4. Logout to secure your session

## Security Features

- Password hashing
- Session management
- CSRF protection
- Secure database operations

## Environment Variables

The application uses the following environment variables for configuration:

Required:
- `DATABASE_URL`: Database connection URL for SQLAlchemy

Optional:
- `PORT`: Server port (default: 5001)
- `SECRET_KEY`: Flask session security key (default: auto-generated)

### Configuration Methods

1. Using .env file:
   - Copy `.env.template` to `.env`
   - Update the values in `.env` with your configuration
   - The application will automatically load these values on startup

2. Using Replit's Secrets tool:
   - For production environments
   - Overrides values in .env file

Note: The .env file is ignored by git for security purposes.