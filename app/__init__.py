from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__) 
app.config.from_object('config')
db = SQLAlchemy(app)



import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from app.config import basedir

lm = LoginManager()
lm.setup_app(app)
oid = OpenID(app,os.path.join(basedir,'tmp'))
lm.login_view = 'login'

from app import models,views