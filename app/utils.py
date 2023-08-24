from functools import wraps
from typing import cast
from flask import flash, redirect, request, url_for
from flask_login import current_user
from app.models import Event, User

current_user = cast(User, current_user)

def event_access_required(f):
    """
    Ein Decorator, um den Zugriff auf Event-bezogene Funktionen zu kontrollieren.

    Dieser Decorator prüft, ob der aktuelle Benutzer der Ersteller des angegebenen Events ist.
    Wenn der Benutzer nicht der Ersteller ist oder das Event nicht existiert, wird eine Fehlermeldung
    angezeigt, und der Benutzer wird auf die vorherige Seite oder die Index-Seite weitergeleitet.

    :param f: Die zu dekorierende Funktion.
    :return: Die dekorierte Funktion.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        event_id = kwargs.get("id")
        if event_id is None:
            flash("Event ID nicht angegeben", "error")
            return redirect(url_for("index"))

        event = Event.query.get(event_id)
        if not event or event.created_by != current_user.id:
            flash(
                "Dieses Event existiert nicht oder Sie haben keinen Zugriff darauf",
                "error",
            )
            return redirect(request.referrer or url_for("index"))

        return f(*args, **kwargs)

    return decorated_function
