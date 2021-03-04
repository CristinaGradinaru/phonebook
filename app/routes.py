from app import app, db, mail, Message
from flask import render_template, request, flash, redirect, url_for
from app.forms import UserInfoForm, LoginForm
from app.models import User
from flask_login import login_user,logout_user, login_required
from werkzeug.security import check_password_hash

@app.route('/')
@app.route('/index')
def index():
    context={
        'title': 'Phonebook | HOME',
        'addentry': {
            1: 'Create an account with us',
            2: 'Add your phone to our virtual phonebook',
            3: 'We will make sure you will NOT be contacted by telemarketers, spammers, scammers etc.'
        }
    }
    return render_template('index.html', **context)

@app.route('/registerphone', methods =['GET', 'POST'])
def register():
    title = "Phonebook | REGISTER"
    form = UserInfoForm()
    if request.method == "POST" and form.validate():
        username= form.username.data
        password= form.password.data
        email = form.email.data
        phone= form.phone.data

        new_user=User(username, email, phone, password)
        db.session.add(new_user)
        db.session.commit()

        welcome = Message(f'Welcome, {username}', [email])
        welcome.html = '<p>Thank you for signing up! Your phone is now in our phonebook</p>'
        mail.send(welcome)
        flash ("You have added your entry", "success")
        return redirect(url_for("index"))
    return render_template('registerphone.html', title= title, form=form)

@app.route('/phonebook')
@login_required
def phonebook():
    context={
        'title': 'Phonebook | Phonebook',
        'addentry': {
            1: 'Create an account with us',
            2: 'Add your phone to our virtual phonebook',
            3: 'We will make sure you will NOT be contacted by telemarketers, spammers, scammers etc.'
        }
    }
    return render_template('phonebook.html', **context)

@app.route('/login', methods = ["GET", "POST"])
def login():
    title= "Phonebook | LOGIN"
    form= LoginForm()
    if request.method=="POST" and form.validate():
        username= form.username.data
        password = form.password.data
        
        user = User.query.filter_by(username=username).first()

        if user is None or not check_password_hash(user.password, password):
           flash("Incorrect Email/Password. Try again", "danger")
           return redirect(url_for('login'))
 
        login_user(user, remember=form.remember_me.data)
        flash("You have successfully logged in!", 'success')
        return redirect(url_for('index'))
 
    return render_template('login.html', title=title, form = form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged OUT!', 'primary')
    return redirect(url_for('index'))