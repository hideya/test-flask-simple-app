from flask import render_template, redirect, url_for, flash, request, jsonify
from datetime import datetime
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from models import User, Memo
from forms import LoginForm, RegistrationForm
import logging

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    try:
        return db.session.get(User, int(id))
    except Exception as e:
        logging.error(f"Error loading user: {str(e)}")
        return None

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('memo'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('memo'))

    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            # Check if username already exists
            if User.query.filter_by(username=form.username.data).first():
                flash('Username already exists. Please choose a different username.', 'danger')
                return render_template('register.html', form=form)
            
            # Check if email already exists
            if User.query.filter_by(email=form.email.data).first():
                flash('Email already registered. Please use a different email.', 'danger')
                return render_template('register.html', form=form)
            
            # Create new user
            user = User(
                username=form.username.data,
                email=form.email.data,
                password_hash=generate_password_hash(form.password.data)
            )
            
            # Add and flush to get the user ID
            db.session.add(user)
            db.session.flush()
            
            # Create empty memo for the user
            memo = Memo(user_id=user.id, content="")
            db.session.add(memo)
            
            # Commit the transaction
            db.session.commit()
            
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
            
        except Exception as e:
            db.session.rollback()
            logging.error(f"Registration error: {str(e)}")
            flash('Registration failed. Please try again.', 'danger')
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('memo'))
    
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(username=form.username.data).first()
            if user and check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                return redirect(url_for('memo'))
            flash('Invalid username or password', 'danger')
        except Exception as e:
            logging.error(f"Login error: {str(e)}")
            flash('An error occurred during login. Please try again.', 'danger')
    
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    try:
        logout_user()
        return redirect(url_for('login'))
    except Exception as e:
        logging.error(f"Logout error: {str(e)}")
        flash('An error occurred during logout.', 'danger')
        return redirect(url_for('memo'))

@app.route('/memo', methods=['GET'])
@login_required
def memo():
    try:
        user_memo = current_user.memo
        if not user_memo:
            user_memo = Memo(user_id=current_user.id, content="")
            db.session.add(user_memo)
            db.session.commit()
        return render_template('memo.html', memo=user_memo)
    except Exception as e:
        logging.error(f"Error accessing memo: {str(e)}")
        flash('An error occurred while loading your memo.', 'danger')
        return redirect(url_for('index'))

@app.route('/api/save-memo', methods=['POST'])
@login_required
def save_memo():
    try:
        content = request.json.get('content')
        if content is not None:
            memo = current_user.memo
            memo.content = content
            memo.last_modified = datetime.utcnow()
            db.session.commit()
            return jsonify({'status': 'success'})
        return jsonify({'status': 'error', 'message': 'No content provided'}), 400
    except Exception as e:
        logging.error(f"Error saving memo: {str(e)}")
        return jsonify({'status': 'error', 'message': 'Failed to save memo'}), 500