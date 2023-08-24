# Importieren der notwendigen Klassen und Funktionen aus den Flask-WTF-Bibliotheken
from flask_wtf import FlaskForm
from wtforms.fields import (
    DateTimeLocalField,
    EmailField,
    IntegerField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import (
    EqualTo,
    InputRequired,
    Length,
    DataRequired,
    NumberRange,
    Optional,
)

# Importieren der Event-Typen und Veranstaltungsorte aus dem Modul app.models
from app.models import EventType, Location


# Definieren einer FlaskForm-Unterklasse namens EventForm
class EventForm(FlaskForm):
    # Dropdown-Feld für den Veranstaltungstyp
    event_type = SelectField(
        "Veranstaltungstyp",
        description="Wählen Sie den Typ der Veranstaltung aus.",
        choices=[
            (member.name, member.value) for member in EventType
        ],  # Verfügbare Event-Typen aus dem EventType-Enum
        validators=[
            InputRequired("Bitte wählen Sie einen Veranstaltungstyp aus.")
        ],  # Erforderliche Eingabe
    )

    # Textfeld für den Namen der Veranstaltung
    name = StringField(
        "Name",
        description="Geben Sie ihrer Veranstaltung einen Namen.",
        validators=[
            InputRequired("Dieses Feld ist erforderlich."),
            Length(
                min=3,
                max=128,
                message="Der Name muss zwischen 3 und 128 Zeichen lang sein.",
            ),
        ],
    )

    # Textfeld für die Beschreibung der Veranstaltung (optional)
    description = TextAreaField(
        "Beschreibung",
        description="Geben Sie eine kurze Beschreibung der Veranstaltung ein.",
        validators=[Optional()],  # Nicht erforderlich
    )

    # Datum und Uhrzeit für den Veranstaltungsbeginn
    start = DateTimeLocalField(
        "Startzeit",
        format="%Y-%m-%dT%H:%M",
        description="Geben Sie das Startdatum und die -zeit der Veranstaltung an.",
        validators=[
            InputRequired("Bitte wählen Sie ein Startdatum und eine Startzeit.")
        ],  # Erforderliche Eingabe
    )

    # Datum und Uhrzeit für das Veranstaltungsende
    end = DateTimeLocalField(
        "Endzeit",
        format="%Y-%m-%dT%H:%M",
        description="Geben Sie das Enddatum und die -zeit der Veranstaltung an.",
        validators=[
            InputRequired("Bitte wählen Sie ein Enddatum und eine Endzeit.")
        ],  # Erforderliche Eingabe
    )

    # Dropdown-Feld für den Veranstaltungsort
    location = SelectField(
        "Veranstaltungsort",
        description="Wählen Sie den Veranstaltungsort aus.",
        choices=[
            (member.name, member.value) for member in Location
        ],  # Verfügbare Veranstaltungsorte aus dem Location-Enum
        validators=[
            InputRequired("Bitte wählen Sie einen Veranstaltungsort aus.")
        ],  # Erforderliche Eingabe
    )

    # Textfeld für eventuelle Essenswünsche (optional)
    food_wish = StringField(
        "Essenswunsch",
        description="Geben Sie eventuelle Essenswünsche an.",
        validators=[Optional()],  # Nicht erforderlich
    )

    # Dropdown-Feld für die Auswahl eines DJs (optional)
    dj = SelectField(
        "DJ",
        description="Wählen Sie den DJ für die Veranstaltung aus.",
        validators=[Optional()],  # Nicht erforderlich
    )

    # Eingabefeld für die Anzahl der Teilnehmer (optional)
    number_of_attendants = IntegerField(
        "Anzahl der Teilnehmer",
        validators=[
            NumberRange(min=0, message="Die Anzahl der Teilnehmer muss positiv sein."),
            Optional(),  # Nicht erforderlich
        ],
    )

    # Button zum Erstellen der Veranstaltung
    submit = SubmitField("Erstellen")


# Definieren einer FlaskForm-Unterklasse namens SigninForm für den Anmeldevorgang
class SigninForm(FlaskForm):
    # Eingabefeld für die E-Mail-Adresse
    email = EmailField(
        "E-Mail-Adresse",
        description="Bitte geben Sie Ihre E-Mail-Adresse ein.",
        validators=[InputRequired()],  # Erforderliche Eingabe
    )

    # Eingabefeld für das Passwort
    password = PasswordField(
        "Passwort",
        description="Bitte geben Sie Ihr Passwort ein.",
        validators=[InputRequired()],  # Erforderliche Eingabe
    )

    # Button zum Anmelden
    submit = SubmitField("Anmelden")


# Definieren einer FlaskForm-Unterklasse namens SignupForm für den Registrierungsvorgang
class SignupForm(FlaskForm):
    # Eingabefeld für die E-Mail-Adresse
    email = EmailField(
        "E-Mail-Adresse",
        description="Bitte geben Sie Ihre E-Mail-Adresse ein.",
        validators=[InputRequired()],  # Erforderliche Eingabe
    )

    # Eingabefeld für das Passwort mit Bestätigung
    password = PasswordField(
        label="Passwort",
        description="Bitte geben Sie Ihr Passwort ein.",
        validators=[
            DataRequired(),  # Erforderliche Eingabe
            Length(min=6, max=10),  # Mindest- und Höchstlänge des Passworts
            EqualTo(
                "confirm", message="Die Passwörter müssen übereinstimmen."
            ),  # Passwortbestätigung prüfen
        ],
    )

    # Eingabefeld zur Bestätigung des Passworts
    confirm = PasswordField(
        label="Passwort bestätigen",
        description="Bitte bestätigen Sie Ihr Passwort.",
    )

    # Button zur Registrierung
    submit = SubmitField("Registrieren")
