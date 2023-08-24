from flask_login import UserMixin
from bcrypt import hashpw, checkpw
from app import app, db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.BINARY(60), nullable=False)

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password: str):
        self.password_hash = hashpw(password.encode(), app.config["PASSWORD_SALT"])

    def verify_password(self, password: str):
        return checkpw(password.encode(), self.password_hash)