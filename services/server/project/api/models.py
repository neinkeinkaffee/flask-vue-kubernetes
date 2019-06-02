import datetime

from flask import current_app
from sqlalchemy.sql import func

from project import db

class Flashcard(db.Model):

    __tablename__ = 'flashcards'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chinese = db.Column(db.String(255), nullable=False)
    english = db.Column(db.String(255), nullable=False)

    def __init__(self, chinese, english):
        self.chinese = chinese
        self.english = english

    def to_json(self):
        return {
            'id': self.id,
            'chinese': self.chinese,
            'english': self.english
        }