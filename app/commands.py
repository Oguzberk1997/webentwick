from datetime import datetime
import click

from app import app, db
from app.models import DJ, Event, EventType, Location, User


@click.command("init-db")
def init():
    with app.app_context():
        db.drop_all()
        db.create_all()
    click.echo("Database has been initialized.")


@click.command("insert-sample-data")
def insert_sample_data():
    # Delete all existing data, if any
    db.session.execute(db.delete(User))
    db.session.execute(db.delete(Event))
    db.session.execute(db.delete(DJ))

    user1 = User(id=1, email="benutzer@example.com")
    user1.password = "passwort123"

    dj1 = DJ(id=1, name="DJ Müller")
    dj2 = DJ(id=2, name="DJ Schmidt")
    dj3 = DJ(id=3, name="DJ Wagner")

    event1 = Event(
        event_type=EventType.WEDDING,
        created_by=user1.id,
        name="Hochzeit von Anna und Peter",
        description="Eine wundervolle Hochzeitsfeier im Sommer.",
        start=datetime(2023, 8, 28, 8),
        end=datetime(2023, 8, 28, 16),
        location=Location.TINKLING_TRAMS_LULLABY,
        food_wish="Buffet mit internationalen Spezialitäten",
        dj=dj1.id,
        number_of_attendants=80,
    )
    event2 = Event(
        event_type=EventType.ENGAGEMENT,
        created_by=user1.id,
        name="Verlobungsfeier von Lisa und Markus",
        description="Eine Feier, um die Verlobung des glücklichen Paares zu feiern.",
        start=datetime(2023, 9, 15, 18),
        end=datetime(2023, 9, 15, 23),
        location=Location.SPREE_SERENADE,
        food_wish="Catering mit Fingerfood",
        dj=dj2.id,
        number_of_attendants=50,
    )
    event3 = Event(
        event_type=EventType.BIRTHDAY,
        created_by=user1.id,
        name="Geburtstagsfeier von Markus",
        description="Eine fröhliche Geburtstagsfeier mit Freunden und Familie.",
        start=datetime(2023, 10, 5, 15),
        end=datetime(2023, 10, 5, 21),
        location=Location.BRANDENBURG_BALLAD,
        food_wish="Barbecue-Party im Garten",
        dj=dj3.id,
        number_of_attendants=30,
    )

    db.session.add_all([user1, dj1, dj2, dj3, event1, event2, event3])
    db.session.commit()

    click.echo("Inserted sample data.")


app.cli.add_command(init)
app.cli.add_command(insert_sample_data)
