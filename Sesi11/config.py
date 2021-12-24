import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'people.db')
##untuk deploy ke heroku di ganti database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://haihlfjhwlzczt:6caa8f55d61c879d41bcde058362e6bb7364a6b07165e26a5e49a4ae3d45a166@ec2-3-209-42-36.compute-1.amazonaws.com:5432/ddmleln67kv10'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)