from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
from models.vacina import Vacina

vacinaroute = Blueprint('vacinaroute', __name__)


@vacinaroute.route('/')
def index():
    return render_template('index.html')


@vacinaroute.route('/vacina/')
def vacina():
    vacinas = Vacina.query.all()
    return render_template('vacina/vacina_lista.html', titulo="Vacinas", vacinas=vacinas)


@vacinaroute.route('/vacina/novo')
def vacina_novo():
    return render_template("vacina/vacina_novo.html", titulo="Nova Vacina.")


@vacinaroute.route('/vacina/criar', methods=['POST', ])
def vacina_criar():
    nome = request.form['nome']
    vacina = Vacina(nome=nome)
    db.session.add(vacina)
    db.session.commit()
    return redirect(url_for('vacinaroute.vacina'))


@vacinaroute.route('/vacina/editar/<id>')
def vacina_editar(id):
    vacina = Vacina.query.filter_by(id=id).first()
    return render_template('vacina/vacina_editar.html', vacina=vacina)


@vacinaroute.route('/vacina/atualizar/<id>', methods=['POST'])
def vacina_atualizar(id):
    nome = request.form['nome']
    vacina = Vacina.query.filter_by(id=id).first()
    vacina.nome = nome
    db.session.commit()
    return redirect(url_for("vacinaroute.vacina"))


@vacinaroute.route('/vacina/excluir/<int:id>', methods=['DELETE', 'GET'])
def vacina_excluir(id):
    vacina = Vacina.query.filter_by(id=id).first()
    db.session.delete(vacina)
    db.session.commit()
    return redirect(url_for('vacinaroute.vacina'))
