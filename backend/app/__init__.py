from flask import Flask
from flask_sqlalchemy import SQLAlchemy

api = Flask(__name__)


# Configurações da aplicação
api.config['DEBUG'] = True
api.config['SECRET_KEY'] = 'a secret key'

# Caminho para a base de dados usada
api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# SQLAlchemy monitorará modificações de objetos
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Objeto SqlAlchemy
db = SQLAlchemy(api)

from app import services
from app import routes
from app import models