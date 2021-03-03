from app import app
from flask import render_template, request
from app.forms import UserInfoForm

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
    if request.method== "POST" and form.validate():
        username= form.username.data
        password= form.password.data
        email = form.email.data
        phone= form.phone.data
        print(username, password, phone, email)
    return render_template('registerphone.html', title= title, form=form)

@app.route('/phonebook')
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