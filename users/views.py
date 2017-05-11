from gift_list import app
from flask import render_template, redirect, url_for, session, request
from users.form import RegisterForm, LoginForm
from users.models import User
from gift_list import db
from users.decorators import login_required
import bcrypt





    
@app.route('/login', methods = ("GET", "POST"))
def login():
    form = LoginForm()
    error = None
    if request.method == 'GET' and request.args.get('next'):
        session["next"] = request.args.get('next', None)
    
    if form.validate_on_submit():
        
        users = User.query.filter_by(
            name = form.name.data
            ).limit(1)
        if users.count():
            user = users[0]
            if bcrypt.hashpw(form.password.data, user.password) == user.password:
                session['name'] = form.name.data
                if 'next' in session:
                    next = session.get('next')
                    session.pop('next')
                    return redirect(next)
                else:
                    return redirect(url_for('list'))
            else:
                error = "Incorrect Username and password"
        else:
            error = "Incorrect Username and password"
    return render_template('users/login.html', form=form, error=error)
    
    
    
    
@app.route('/register', methods = ("GET", 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        user = User(
            name = form.name.data,
            password = hashed_password
            )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('users/register.html', form=form)
    
@app.route('/success')
def success():
    return "User Registered"
    
@app.route('/login_success')
@login_required
def login_success():
    return "Logged in"
    
@app.route('/logout')
def logout():
    if session.get('name'):
        session.pop('name')
    return redirect(url_for('index'))
    