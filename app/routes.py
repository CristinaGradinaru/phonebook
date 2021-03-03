from app import app
from flask import render_template, request
from app.forms import UserInfoForm

@app.route('/')
@app.route('/index')
def index():
    title = "Phonebook | HOME "
    return render_template('index.html', title = title)

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
        'add entry': {
            1: ''
        }
    }
    
    return render_template('phonebook.html', **context)