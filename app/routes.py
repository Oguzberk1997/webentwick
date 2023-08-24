# Importieren der benötigten Module und Klassen
from typing import List, cast
from flask import flash, jsonify, request, url_for, redirect, render_template, session
from flask_login import logout_user, login_required, login_user, current_user
from sqlalchemy.orm import events
from app import app, db
from app.models import DJ, Event, EventType, Location, User
from app.forms import EventForm, SigninForm, SignupForm
from app.utils import event_access_required

current_user = cast(User, current_user)

# Startseite - zeigt einfach die Indexseite an
@app.route("/")
def index():
    return render_template("index.html")


# Anzeige der Events des angemeldeten Benutzers
@app.route("/my-events", methods=["GET"])
@login_required  # Benutzer muss angemeldet sein, um auf diese Seite zuzugreifen
def my_events():
    return render_template("my-events.html", events=current_user.events)


# Erstellen eines neuen Events
@app.route("/new-event", methods=["GET", "POST"])
@login_required  # Benutzer muss angemeldet sein, um auf diese Seite zuzugreifen
def new_event():
    form = EventForm()

    # Setzen der Auswahlmöglichkeiten für DJs im Formular
    form.dj.choices = [
        (dj.id, dj.name) for dj in db.session.execute(db.select(DJ)).scalars()
    ]

    if form.validate_on_submit():
        # Erstellen eines neuen Event-Objekts basierend auf Formulardaten
        new_event = Event(
            created_by=current_user.get_id(),
            event_type=EventType[form.event_type.data or "WEEDING"],
            name=form.name.data,
            description=form.description.data,
            start=form.start.data,
            end=form.end.data,
            location=Location[form.location.data or "TINKLING_TRAMS_LULLABY"],
            food_wish=form.food_wish.data,
            dj=form.dj.data,
            number_of_attendants=form.number_of_attendants.data,
        )

        # Hinzufügen und Speichern des neuen Event-Objekts in der Datenbank
        db.session.add(new_event)
        db.session.commit()

        flash("Neues Event hinzugefügt", "success")  # Zeige Erfolgsmeldung an

        return redirect(url_for("my_events"))

    return render_template("new-event.html", form=form)


# Anzeigen eines bestimmten Events
@app.route("/view-event/<int:id>", methods=["GET"])
@login_required  # Benutzer muss angemeldet sein, um auf diese Seite zuzugreifen
@event_access_required  # Benutzer muss berechtigt sein, dieses Event anzuzeigen
def view_event(id):
    event = db.session.get(Event, id)

    return render_template("view-event.html", event=event)


# Löschen eines bestimmten Events
@app.route("/delete-event/<int:id>", methods=["GET"])
@login_required  # Benutzer muss angemeldet sein, um auf diese Seite zuzugreifen
@event_access_required  # Benutzer muss berechtigt sein, dieses Event zu löschen
def delete_event(id):
    event = db.session.get(Event, id)

    # Löschen des Event-Objekts aus der Datenbank
    db.session.delete(event)
    db.session.commit()

    flash("Event wurde gelöscht", "warning")  # Zeige Warnungsmeldung an

    return redirect(url_for("my_events"))


# Anmeldeseite
@app.route("/signin", methods=["GET", "POST"])
def signin():
    print(type(current_user))
    if current_user.is_authenticated:
        return redirect(
            url_for("index")
        )  # Falls Benutzer bereits angemeldet ist, leite um

    form = SigninForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)  # Benutzer anmelden
            session.permanent = True

            flash("Erfolgreich angemeldet", "success")  # Zeige Erfolgsmeldung an

            next_page = request.args.get("next")
            return redirect(next_page or url_for("my_events"))

        flash(
            "Ungültige E-Mail-Adresse oder Passwort", "error"
        )  # Zeige Fehlermeldung an

    return render_template("signin.html", form=form)


# Registrierungsseite
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(
            url_for("index")
        )  # Falls Benutzer bereits angemeldet ist, leite um

    form = SignupForm()

    if form.validate_on_submit():
        if not User.query.filter_by(email=form.email.data).first():
            new_user = User(email=form.email.data)
            new_user.password = form.password.data
            db.session.add(new_user)
            db.session.commit()

            flash("Benutzer erstellt", "success")  # Zeige Erfolgsmeldung an

            return redirect(url_for("signin"))

        flash("Dieser Benutzer existiert bereits", "error")  # Zeige Fehlermeldung an

    return render_template("signin.html", form=form, is_signup=True)


# Abmelden des Benutzers
@app.route("/signout")
@login_required  # Benutzer muss angemeldet sein, um abzumelden
def signout():
    logout_user()  # Benutzer abmelden
    flash("Sie wurden abgemeldet", "success")  # Zeige Erfolgsmeldung an
    return redirect(url_for("index"))

# Schnittstelle für Events
@app.route("/api/events")
@login_required  # Benutzer muss angemeldet sein, um abzumelden
def get_events():
    events = cast(List[Event], current_user.events)
    return jsonify([event.serialize() for event in events])

# Testroute zum Anzeigen von Toast-Nachrichten
@app.route("/test/toasts")
def test_toasts():
    messages = [
        ("Dies ist eine Erfolgsmeldung", "success"),
        ("Dies ist eine Warnungsmeldung", "warning"),
        ("Dies ist eine Fehlermeldung", "error"),
    ]

    for message, category in messages:
        flash(message, category)  # Zeige Test-Toasts an

    return render_template("index.html")


# Behandlung von 404-Fehlern (Seite nicht gefunden)
@app.errorhandler(404)
def http_not_found(_):
    return render_template("404.html"), 404


# Behandlung von 500-Fehlern (interner Serverfehler)
@app.errorhandler(500)
def http_internal_server_error(_):
    return render_template("500.html"), 500
