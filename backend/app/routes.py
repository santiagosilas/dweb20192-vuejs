from flask import render_template
from flask import jsonify
from app import api

payments = [
    {'id':11, 'description': 'CREDIT_CARD'},
    {'id':12, 'description': 'BOLETO'}
]

@api.route('/api/payments')
def getPayments():
    return jsonify({'data': payments})

@api.route('/')
@api.route('/home')
def home():
    message = 'Hello World'
    return render_template('Index.html', 
        msg = message)

@api.route('/contact')
def contact():
    return 'contact'