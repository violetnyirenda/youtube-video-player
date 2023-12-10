from flask import Flask, request, jsonify
from pymongo import MongoClient

mongo_uri = 'mongodb://localhost:27017/'
db_name = 'library'


client = MongoClient(mongo_uri)
db = client[db_name]
collection_books = db["books"]
collection_user = db["users"]

app=Flask(__name__)

@app.route('/create-book', methods=['POST'])
def create_book():
    body = request.get_json()

    collection_books.insert_one(body)
    
    return "hey"


@app.route('/create-user', methods=['POST'])
def create_user():
    body = request.get_json()
    
    collection_user.insert_one(body)

    return "okay"


@app.route('/get-user', methods=['POST'])
def get_user():
    body = request.get_json()
    user = list(collection_user.find({'name':body['name'], "password":body["password"]}))
    for doc in user:
        doc['_id'] = str(doc['_id'])

    return jsonify(user)

@app.route('/get-book', methods=['GET'])
def get_book():
    
    books = list(collection_books.find())
    for doc in books:
        doc['_id'] = str(doc['_id'])

    return jsonify(books)



@app.route('/get-book-name', methods=['POST'])
def get_book_by_name():
    body = request.get_json()
    books = list(collection_books.find({"name":body["name"]}))
    for doc in books:
        doc['_id'] = str(doc['_id'])

    return jsonify(books)

if __name__=='__main__':
    app.run(debug=True)