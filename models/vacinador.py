import re

from extensions import db


class Vacinador(db.Model):
    crm = db.Column(db.String(15), primary_key=True)
    cpf = db.Column(db.String(12), nullable=False, unique=True)
    nome = db.Column(db.String(128), nullable=False)
    dtNascimento = db.Column(db.Date, nullable=False)
    aplicacao = db.relationship('Aplicacao', backref='vacinador', cascade="all, delete", passive_deletes=False, lazy=True)

    @staticmethod
    def trazer_crm(param):
        txt = re.search("([A-Z|a-z]{3})([A-Z|a-z]{2})([0-9]{6})", param)
        txt = f"{txt.group(1)}/{txt.group(2)} {txt.group(3)}"
        return txt.upper()

    @staticmethod
    def add_crm_banco(param: str) -> str:
        param = param.upper()
        param = re.sub(r"\s+", "", param)
        crm = re.search("([A-Z]{3})(/)([A-Z]{2})([0-9]{6})", param)
        crm = crm.group(1) + crm.group(3) + crm.group(4)
        return crm.upper()
