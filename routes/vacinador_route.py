from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for

from extensions import db
from models.vacinador import Vacinador

vacinador_route = Blueprint('vacinador_route', __name__)


@vacinador_route.route('/vacinador')
def vacinador():
    lista = Vacinador.query.all()
    for vacinador in lista:
        vacinador.crmtemplate = Vacinador.trazer_crm(vacinador.crm)
    return render_template('vacinador/vacinador_lista.html', titulo="Lista de vacinadores", vacinadores=lista)


@vacinador_route.route('/vacinador/novo')
def vacinador_novo():
    return render_template("vacinador/vacinador_novo.html", titulo="Novo vacinador")


@vacinador_route.route('/vacinador/criar', methods=['POST', ])
def vacinador_criar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    crm = Vacinador.add_crm_banco(request.form['crm'])
    dt_nascimento = datetime.strptime(request.form['nascimento'], '%Y-%m-%d').date()

    vacinador = Vacinador(nome=nome, cpf=cpf, crm=crm, dtNascimento=dt_nascimento)
    db.session.add(vacinador)
    db.session.commit()
    return redirect(url_for('vacinador_route.vacinador'))


@vacinador_route.route('/vacinador/atualizar/<string:crm>', methods=['POST', ])
def vacinador_atualizar(crm):
    vacinador = Vacinador.querry.filter_by(crm=crm).first()
    if vacinador:
        vacinador.nome = request.form['nome']
        vacinador.cpf = request.form['cpf']
        vacinador.dt_nascimento = datetime.strptime(request.form['nascimento'], '%Y-%m-%d').date()
        db.session.commit()
    return redirect(url_for('vacinador_route.vacinador'))


@vacinador_route.route('/vacinador/editar/<string:crm>')
def vacinador_editar(crm):
    vacinador = Vacinador.query.filter_by(crm=crm).first()
    return render_template("vacinador/vacinador_editar.html", titulo="Editando Vacinador", vacinador=vacinador)


@vacinador_route.route('/vacinador/excluir/<string:crm>', methods=['DELETE', 'GET'])
def vacinador_excluir(crm):
    vacinador = Vacinador.query.filter_by(crm=crm).first()
    db.session.delete(vacinador)
    db.session.commit()
    return redirect(url_for('vacinador_route.vacinador'))

