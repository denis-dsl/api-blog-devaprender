from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy


def inicializar():
    app = Flask(__name__)
    # Configurações inicias
    app.config['SECRET_KEY'] = 'segredo2030'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres.ixmdvajbzeggegklhpeq:bLudHuyoYZPEr83K@aws-0-us-west-1.pooler.supabase.com:5432/postgres'

    db = SQLAlchemy(app)
    db: SQLAlchemy

    class Postagem(db.Model):
        __tablename__ = 'postagem'
        id_postagem = db.Column(db.Integer, primary_key=True)
        titulo = db.Column(db.String)
        id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

    class Autor(db.Model):
        __tablename__ = 'autor'
        id_autor = db.Column(db.Integer, primary_key=True)
        nome = db.Column(db.String)
        email = db.Column(db.String)
        senha = db.Column(db.String)
        admin = db.Column(db.Boolean)
        postagens = db.relationship('Postagem')

    with app.app_context():
        db.drop_all()
        db.create_all()
        autor = Autor(nome='Jhonatan', email='jhonatan@hotmail.com',
                      senha='senha123', admin=True)
        db.session.add(autor)
        db.session.commit()


if __name__ == '__main__':
    inicializar()
