from flask_wtf import FlaskForm
from wtforms.fields import (
    DateTimeLocalField,
    EmailField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import EqualTo, InputRequired, Length, DataRequired

from app.models import EventType


class NewEventForm(FlaskForm):
    event_type = SelectField(
        "Event type",
        description="todo!",
        choices=[
            (name, member.value) for name, member in EventType.__members__.items()
        ],
    )
    name = StringField("Name", validators=[InputRequired(), Length(min=3, max=128)])
    description = TextAreaField("Description")
    start = DateTimeLocalField("Start", format='%Y-%m-%dT%H:%M')
    end = DateTimeLocalField("End", format='%Y-%m-%dT%H:%M')
    submit = SubmitField("Erstellen")


class SigninForm(FlaskForm):
    email = EmailField(
        "E-Mail-Adresse",
        description="Bitte geben Sie Ihre E-Mail-Adresse ein.",
        validators=[InputRequired()],
    )
    password = PasswordField(
        "Passwort",
        description="Bitte geben Sie Ihr Passwort ein.",
        validators=[InputRequired()],
    )
    submit = SubmitField("Anmelden")


class SignupForm(FlaskForm):
    email = EmailField(
        "E-Mail-Adresse",
        description="Bitte geben Sie Ihre E-Mail-Adresse ein.",
        validators=[InputRequired()],
    )
    password = PasswordField(
        label="Passwort",
        description="Bitte geben Sie Ihr Passwort ein.",
        validators=[
            DataRequired(),
            Length(min=6, max=10),
            EqualTo("confirm", message="Die Passwörter müssen übereinstimmen."),
        ],
    )
    confirm = PasswordField(
        label="Passwort bestätigen",
        description="Bitte bestätigen Sie Ihr Passwort.",
    )
    submit = SubmitField("Registrieren")
