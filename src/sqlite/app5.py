"""
build CRUD online services
"""
from flask import Flask, jsonify, request
import json
# from flask_cors import CORS
from sqlitebookdb import * 
import uuid

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
# CORS(app)
app.config.from_object(__name__)
db = BookDB('sqlitebook.db')

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books', methods=['GET'])
def all_books():
    response_object = {'status': 'success'}
    books = db.getBooks()
    print(books)
    response_object['books'] = books
    return jsonify(response_object)
    
@app.route('/books', methods=['POST'])
def create_book():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    book = {
        '_id': uuid.uuid4().hex,
        'title': post_data.get('title'),
        'author': post_data.get('author'),
        'read': post_data.get('read'),
        'price': post_data.get('price'),
        'rating': post_data.get('rating'),
    }
    id = db.create(book)
    response_object['message'] = 'Book added!'
    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['GET'])
def retrieve_book(book_id):
    response_object = {'status': 'success'}
    post_data = request.get_json()
    book = db.getBook(book_id)
    response_object['book'] = book
    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    response_object = {'status': 'success'}
    post_data = request.get_json()
    id = db.delete(book_id)
    response_object['message'] = 'Book deleted!'
    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    response_object = {'status': 'success'}
    post_data = request.get_json()
    book = {
        'title': post_data.get('title'),
        'author': post_data.get('author'),
        'read': post_data.get('read'),
        'price': post_data.get('price'),
        "rating":post_data.get("rating")
    }
    db.update(book_id, book)
    response_object['message'] = 'Book updated!'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(host="localhost", port=5000)