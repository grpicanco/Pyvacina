from extensions import db


class Aplicacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crm = db.Column(db.String(15), db.ForeignKey('vacinador.crm', ondelete="CASCADE"), nullable=False)
    cns = db.Column(db.String(15), db.ForeignKey('vacinado.cns', ondelete="CASCADE"), nullable=False)
    id_vacina = db.Column(db.Integer, db.ForeignKey('vacina.id', ondelete="CASCADE"), nullable=False)
    data = db.Column(db.Date, nullable=False)
