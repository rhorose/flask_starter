from flask import Flask
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)
app.config.from_object(Config)
from app import views
db = SQLAlchemy(app)
migrate = Migrate(app,db)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
