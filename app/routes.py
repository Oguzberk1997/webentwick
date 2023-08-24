from flask import flash, request, url_for, redirect, render_template, session
from flask_login import logout_user, login_required, login_user, current_user

from app import app, db
from app.models import Event, EventType, User
from app.forms import NewEventForm, SigninForm, SignupForm


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def http_not_found(_):
    return render_template("404.html"), 404


@app.errorhandler(500)
def http_internal_server_error(_):
    return render_template("500.html"), 500


@app.route("/new-event", methods=["GET", "POST"])
@login_required
def new_event():
    form = NewEventForm()

    if form.validate_on_submit():
        new_event = Event(
            name=form.name.data,
            event_type=EventType[form.event_type.data or "WEEDING"],
            description=form.description.data,
            start=form.start.data,
            end=form.end.data,
            created_by=current_user.get_id(),
        )

        db.session.add(new_event)
        db.session.commit()

        flash("Neues Event hinzugefügt", "success")

    return render_template("new-event.html", form=form)


@app.route("/my-events", methods=["GET"])
@login_required
def my_events():
    return render_template("my-events.html", events=current_user.events)


@app.route("/edit-event/<int:id>", methods=["GET"])
@login_required
def edit_event(id):
    event = db.session.get(Event, id)

    if not event or event.created_by != current_user.id:
        flash("This event does not exsits", "error")

        return redirect(request.referrer or url_for("index"))

    return render_template("edit-event.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = SigninForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)
            session.permanent = True

            flash("Erfolgreich angemeldet", "success")

            next_page = request.args.get("next")
            return redirect(next_page or url_for("index"))

        flash("Ungültige E-Mail-Adresse oder Passwort", "error")

    return render_template("signin.html", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = SignupForm()

    if form.validate_on_submit():
        if not User.query.filter_by(email=form.email.data).first():
            new_user = User(email=form.email.data)
            new_user.password = form.password.data
            db.session.add(new_user)
            db.session.commit()

            flash("Benutzer erstellt", "success")

            return redirect(url_for("anmelden"))

        flash("Dieser Benutzer existiert bereits", "error")

    return render_template("signin.html", form=form, is_signup=True)


@app.route("/signout")
@login_required
def signout():
    logout_user()
    flash("Sie wurden abgemeldet", "success")
    return redirect(url_for("index"))
