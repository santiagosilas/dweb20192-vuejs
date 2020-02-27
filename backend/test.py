from requests import get, post, put, delete
import json

if __name__ == '__main__':

    url = 'http://localhost:5000/api/books'

    books = get(url).json()
    print('GET {}'.format(url))
    print('Response:', json.dumps(books, indent=1))
    print()

