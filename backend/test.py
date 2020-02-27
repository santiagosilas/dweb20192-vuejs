from requests import get, post, put, delete
import json

if __name__ == '__main__':

    url = 'http://localhost:5000/api/books'

    books = get(url).json()
    print('GET {}'.format(url))
    print('Response:', json.dumps(books, indent=1))
    print()

    # Implementar o test para o POST
    #url = 'http://localhost:5001/api/books'
    #params = {'title':'Vue.js', 'author': 'Fulano de Tal', 'read': False}
    #book = post(url, params).json()
    #print('POST {}'.format(url))
    #print('Body:', json.dumps(params, indent=1))
    #print('Response:', json.dumps(book, indent=1))
    #print()

    # Implementar o test para o DELETE
    # (to do.)

    # Implementar o test para o PUT
    # (to do.)
