from flask import Flask, request, Response
from flask import jsonify

#ceci est un 3ieme commentaire
# ceci est un test dajout


app = Flask(__name__)
#print(__name__)

books = [
   {
       'name' : 'Green Eggs',
       'price': 7.99,
       'isbn' : 978802359600265
   },
   {
       'name' : 'The cat in the hat',
       'price': 6.99,
       'isbn' : 978111359600264
   }
]

#GET / (by default, it's GET)
@app.route('/')
def big_data():
   return 'Big Data!'

@app.route('/hello')
def hello_world():
   return 'Hello World!'

#GET /books ==> lister tous les livres
@app.route('/books')
def get_books():
    result = { "books" : books }
    return jsonify(result)

#GET /books/<isbn> ==> récupérer le détail d'un livre
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    fake_book = { }
    for b in books:
        if b["isbn"] == isbn:
            fake_book["name"] = b["name"]
            fake_book["price"] = b["price"]
            return jsonify(fake_book)
    response = Response("isbn not found", 404, mimetype='application/json')
    return response

#POST /books
@app.route('/books', methods = ['POST'])
def add_book():
   request_data = request.get_json()
   books.insert(0, request_data)
   response = Response("book added successfully", 201, mimetype='application/json')
   return response


#DELETE /books
@app.route('/books/<int:isbn>', methods = ['DELETE'])
def DEL_book(isbn):
    for b in books:
        if b["isbn"] == isbn:
            books.remove(b)
            response = Response("isbn deleted", 204, mimetype='application/json')
            return response
    response = Response("isbn not found", 404, mimetype='application/json')
    return response


app.run(port=5000)
