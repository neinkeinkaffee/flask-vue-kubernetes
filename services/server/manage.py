from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import Flashcard


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(Flashcard(
        chinese='chi le ma?',
        english='Have you eaten?'
    ))
    db.session.add(Flashcard(
        chinese='qu nali a',
        english='Where are you headed?'
    ))
    db.session.commit()


if __name__ == '__main__':
    cli()
