from datetime import datetime
import click

from app import app, db
from app.models import Event, EventType, User


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

    user1 = User(id=1, email="max@musterman.de")
    user1.password = "1234"

    event1 = Event(
        event_type=EventType.WEEDING,
        name="Test event",
        description="todo!",
        start=datetime(2023, 8, 28, 8),
        end=datetime(2023, 8, 28, 16),
        created_by=user1.id,
    )

    db.session.add_all([user1, event1])
    db.session.commit()

    click.echo("Inserted sample data.")


app.cli.add_command(init)
app.cli.add_command(insert_sample_data)
