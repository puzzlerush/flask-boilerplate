from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from blueprints.users import users_blueprint

app.register_blueprint(users_blueprint)

@app.route('/')
def hello():
    return 'Hello World!'
