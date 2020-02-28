from app import db
from app.models import Nota

def drop_db():
    db.drop_all()

def create_db():
    # db.drop_all()
    db.create_all()
    print("Banco criado.")

def populate_db():

    # Insere uma nota no banco
    nota = Nota('lembrete 1', 'Estudar Flask-SqlAlchemy')
    db.session.add(nota)
    db.session.commit()

    # Insere uma nota no banco
    nota = Nota('lembrete 2', 'Estudar Flask-SqlAlchemy')
    db.session.add(nota)
    db.session.commit()

    # Atualiza uma nota
    nota.titulo = 'Estudar Flask-SqlAlchemy'
    db.session.commit()

    # Atualiza uma nota
    nota = Nota.query.all()[0]
    db.session.delete(nota)
    db.session.commit()

    # Obtém todas as notas
    notas = Nota.query.all()
    for nota in notas:
        print('nota:', nota.titulo)

    # Filtrando informações
    notas = Nota.query.filter_by(titulo='Estudar Flask-SqlAlchemy').all()
    print(notas[0].titulo)

    notas = Nota.query.filter_by(titulo='...').all()
    print(notas)