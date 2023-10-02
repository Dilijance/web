from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///message.db'
app.config['SECRET_KEY'] = '43faaca3da39223c8aaec634'
app.app_context().push()
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from base import routes