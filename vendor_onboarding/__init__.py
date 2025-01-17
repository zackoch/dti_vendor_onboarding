import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dotenv

dotenv.load_dotenv()

app = Flask(__name__, static_folder='static-files')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from vendor_onboarding import routes