from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy()

SECRET_KEY='90e5085ea852343f0e319d57e34f2847'

app.config['SECRET_KEY']= SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1712@localhost:5432/znap"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

from Rwood.accounts.routes import accounts
from Rwood.contacts.routes import contacts  
app.register_blueprint(accounts)
app.register_blueprint(contacts)
  