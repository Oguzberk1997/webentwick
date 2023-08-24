from flask import flash, request, url_for, redirect, render_template, session
from flask_login import logout_user, login_required, login_user, current_user

from app import app, db
from app.models import User
from app.forms import SigninForm, SignupForm


@app.route("/")
def index():
    return render_template("index.html")


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

            flash("Erfolgreich angemeldet.", "success")

            next_page = request.args.get("next")
            return redirect(next_page or url_for("index"))

        flash("Ungültige E-Mail-Adresse oder Passwort.", "error")

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

            flash("Benutzer erstellt.", "success")

            return redirect(url_for("anmelden"))

        flash("Dieser Benutzer existiert bereits.", "error")

    return render_template("signin.html", form=form, is_signup=True)


@app.route("/signout")
@login_required
def signout():
    logout_user()
    flash("Sie wurden abgemeldet.", "success")
    return redirect(url_for("index"))
