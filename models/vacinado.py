from extensions import db


class Vacinado(db.Model):
    cns = db.Column(db.String(15), primary_key=True)
    cpf = db.Column(db.String(12), nullable=False, unique=True)
    nome = db.Column(db.String(128), nullable=False)
    dtNascimento = db.Column(db.Date, nullable=False)
    comorbidade = db.Column(db.Boolean, nullable=False)
    qtdDose = db.Column(db.Integer, nullable=False)
    aplicacao = db.relationship('Aplicacao', backref='vacinado', cascade="all, delete", passive_deletes=False, lazy=True)
