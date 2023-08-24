import click
from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.sqlite'

db = SQLAlchemy()
db.init_app(app)

with app.app_context():
    db.create_all()

@click.command('init-db')
def init():  # (1.)
    with app.app_context():
        db.drop_all()
        db.create_all()
    click.echo('Database has been initialized.')

app.cli.add_command(init)  # (2.)

def insert_sample():
    # todo!
    pass
