import os

from flask import Blueprint, jsonify, request

from project.api.models import Flashcard
from project import db


flashcards_blueprint = Blueprint('flashcards', __name__)


@flashcards_blueprint.route('/flashcards', methods=['GET', 'POST'])
def all_flashcards():
    response_object = {
        'status': 'success',
        'container_id': os.uname()[1]
    }
    if request.method == 'POST':
        post_data = request.get_json()
        chinese = post_data.get('chinese')
        english = post_data.get('english')
        db.session.add(Flashcard(chinese=chinese, english=english))
        db.session.commit()
        response_object['message'] = 'Flashcard added!'
    else:
        response_object['flashcards'] = [flashcard.to_json() for flashcard in Flashcard.query.all()]
    return jsonify(response_object)


@flashcards_blueprint.route('/flashcards/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!',
        'container_id': os.uname()[1]
    })


@flashcards_blueprint.route('/flashcards/<flashcard_id>', methods=['PUT', 'DELETE'])
def single_book(flashcard_id):
    response_object = {
      'status': 'success',
      'container_id': os.uname()[1]
    }
    flashcard = Flashcard.query.filter_by(id=flashcard_id).first()
    if request.method == 'PUT':
        post_data = request.get_json()
        flashcard.chinese = post_data.get('chinese')
        flashcard.english = post_data.get('english')
        db.session.commit()
        response_object['message'] = 'Flashcard updated!'
    if request.method == 'DELETE':
        db.session.delete(flashcard)
        db.session.commit()
        response_object['message'] = 'Flashcard removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
