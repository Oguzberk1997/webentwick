from enum import Enum
from flask_login import UserMixin
from bcrypt import hashpw, checkpw
from app import app, db, login_manager


# Definition der Event-Typen als Enum
class EventType(Enum):
    WEDDING = "Hochzeit"
    ENGAGEMENT = "Verlobung"
    BIRTHDAY = "Geburtstagsfeiern"


# Definition der Event-Orte als Enum
class Location(Enum):
    TINKLING_TRAMS_LULLABY = "Klingelnde Straßenbahn Wiegenlied"
    SPREE_SERENADE = "Spree Serenade"
    BRANDENBURG_BALLAD = "Brandenburg Ballade"
    UNTER_DEN_LINDEN_ARIA = "Unter den Linden Arie"
    POTSDAMER_PLATZ_PASSION = "Potsdamer Platz Leidenschaft"


# DJ-Modell
class DJ(db.Model):
    __tablename__ = "djs"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, nullable=False)


# Event-Modell
class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True, index=True)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    event_type = db.Column(db.Enum(EventType), default=EventType.BIRTHDAY)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String, nullable=True)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.Enum(Location), default=Location.TINKLING_TRAMS_LULLABY)
    food_wish = db.Column(db.String, nullable=True)
    dj = db.Column(db.Integer, db.ForeignKey("djs.id"), nullable=True)
    number_of_attendants = db.Column(db.Integer, nullable=False)


# Benutzermodell mit Authentifizierung
class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.BINARY(60), nullable=False)
    events = db.relationship("Event", backref="events", lazy=True)  # Benutzer-Events

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password: str):
        self.password_hash = hashpw(password.encode(), app.config["PASSWORD_SALT"])

    def verify_password(self, password: str):
        return checkpw(password.encode(), self.password_hash)


# Funktion zum Laden eines Benutzers für Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
