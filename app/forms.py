from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import EqualTo, InputRequired, Length, DataRequired


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
