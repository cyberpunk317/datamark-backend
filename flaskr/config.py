from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from yaml import Loader, load


app = Flask(__name__)
app.secret_key = 'aaa'
app.config["UPLOAD_FOLDER"] = "static/uploads"

api = Api(app)

CORS(app)

flask_config = load(open('./config.yaml', 'r'), Loader)
app.config.update(**flask_config)

db = SQLAlchemy(app)
ma = Marshmallow(app)
