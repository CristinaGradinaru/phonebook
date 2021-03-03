from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(150), nullable=False, unique=True)
    email= db.Column(db.String(150), nullable=False, unique=True)
    phone= db.Column(db.String(150), nullable=False, unique=True)
    password= db.Column(db.String(256), nullable= False)

    def __init__(username, email, phone, password):
        self.username = username
        self.email = email
        self.phone = phone
        self.password = generate_password_hash(password)

    

