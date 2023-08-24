from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Erstelle eine Flask-App
app = Flask(__name__)

# Konfiguration der App
app.config.from_mapping(
    SECRET_KEY="secret_key_just_for_dev_environment",  # Geheimer Schlüssel für die App
    PASSWORD_SALT=b"$2b$12$kCXSB0DDlpyZ02nOPPsN3.",  # Salz für Passwörter (kann sicherer sein)
    SQLALCHEMY_DATABASE_URI="sqlite:///data.sqlite",  # Verbindung zur SQLite-Datenbank
)

# Initialisiere die Datenbank
db = SQLAlchemy(app)

# Erstelle die Datenbanktabellen, falls sie noch nicht existieren
with app.app_context():
    db.create_all()

# Initialisiere den Login-Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "signin"  # Die Seite, auf die Benutzer weitergeleitet werden, wenn sie nicht angemeldet sind

# Importiere Routen und Befehle
from app import routes, commands

# Starte die App, wenn dies die Hauptausführungsdatei ist
if __name__ == "__main__":
    app.run(debug=True)  # Starte die App im Debug-Modus
