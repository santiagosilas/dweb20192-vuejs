from flask import render_template
from flask import jsonify
from app import api as app

# uma lista de livros, para simular uma base de dados
books = [
    {'id':1, 'title': 'Python Fluente',  'author': 'Luciano Ramalho', 'read': False},
    {'id':2, 'title': 'Pense em Python',  'author': 'Downey e Gomes', 'read': False},
    {'id':3, 'title': 'Web Scraping Com Python',  'author': 'Mitchell e Kinoshita', 'read': False},
]


@app.route('/api/books', methods=['GET'])    
def get_books():
    return jsonify({'books': books})

@app.route('/api/books/<int:book_id>', methods=['GET']) 
def get_book(book_id):
    pass

@app.route('/api/books', methods=['POST'])
def create_book():
    pass # dica: body em request.form

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    pass # dica: body em request.form

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    pass


@app.route('/')
@app.route('/home')
def home():
    message = 'Hello World'
    return render_template('Index.html', 
        msg = message)

@app.route('/contact')
def contact():
    return 'contact'