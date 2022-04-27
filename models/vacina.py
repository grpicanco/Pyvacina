from extensions import db


class Vacina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128))
    aplicacao = db.relationship('Aplicacao', backref='vacina', cascade="all, delete", passive_deletes=False, lazy=True)
