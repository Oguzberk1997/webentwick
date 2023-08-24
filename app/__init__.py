from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)

app.config.from_mapping(
    SECRET_KEY="secret_key_just_for_dev_environment",
    PASSWORD_SALT=b"$2b$12$kCXSB0DDlpyZ02nOPPsN3.",
    SQLALCHEMY_DATABASE_URI="sqlite:///todos.sqlite",
)

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "signin"

from app import routes, commands

if __name__ == "__main__":
    app.run(debug=True)
