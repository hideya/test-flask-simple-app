from flask import render_template, redirect, url_for, flash, request, jsonify
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

logging.basicConfig(level=logging.DEBUG)

@login_manager.user_loader
def load_user(id):
    return db.session.get(User, int(id))

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
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data)
        )
        try:
            # First commit the user to get their ID
            db.session.add(user)
            db.session.commit()
            
            # Now create memo with the user ID
            memo = Memo(user_id=user.id, content="")
            db.session.add(memo)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Please try again.', 'danger')
            logging.error(f"Registration error: {str(e)}")
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('memo'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('memo'))
        flash('Invalid username or password', 'danger')
    
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/memo', methods=['GET'])
@login_required
def memo():
    user_memo = current_user.memo
    if not user_memo:
        user_memo = Memo(user_id=current_user.id, content="")
        db.session.add(user_memo)
        db.session.commit()
    return render_template('memo.html', memo=user_memo)

@app.route('/api/save-memo', methods=['POST'])
@login_required
def save_memo():
    content = request.json.get('content')
    if content is not None:
        memo = current_user.memo
        memo.content = content
        memo.last_modified = datetime.utcnow()
        db.session.commit()
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'}), 400
