from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash

from Test.vacinadoTest import VacinadoTest
from extensions import db
from models.vacinado import Vacinado

vacinadoroute = Blueprint('vacinadoroute', __name__)


@vacinadoroute.route('/vacinado')
def vacinado():
    lista = Vacinado.query.all()
    return render_template('vacinado/vacinado_lista.html', titulo='Vacinados', vacinados=lista)


@vacinadoroute.route('/vacinado/novo')
def vacinado_novo():
    return render_template('vacinado/vacinado_novo.html', titulo='Novo Vacinado')


@vacinadoroute.route('/criarVacinado', methods=['POST', ])
def vacinado_criar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    cns = request.form['cns']
    dtnascimento = datetime.strptime(request.form['nascimento'], '%Y-%m-%d').date()
    comorbidade = eval(request.form['comorbidade'])
    qtdDose = int(0)

    vacinadoTest = VacinadoTest(nome=nome, cpf=cpf, cns=cns, dtnascimento=dtnascimento, comorbidade=comorbidade,
                                qtdDose=qtdDose)

    if vacinadoTest.value:
        db.session.add(vacinadoTest.vacinado)
        db.session.commit()
        return redirect(url_for('vacinadoroute.vacinado'))
    else:
        flash(vacinadoTest.vacinado, 'alert-danger')
        return redirect(url_for('vacinadoroute.vacinado_novo'))


@vacinadoroute.route('/vacinado/atualizar/<string:cns>', methods=['POST', ])
def vacinado_atualizar(cns):
    vacinado = Vacinado.query.filter_by(cns=cns).first()
    if vacinado:
        vacinado.nome = request.form['nome']
        vacinado.cpf = request.form['cpf']
        vacinado.dtnascimento = datetime.strptime(request.form['nascimento'], '%Y-%m-%d').date()
        vacinado.comorbidade = eval(request.form['comorbidade'])
        vacinado.qtdDose = int(vacinado.qtdDose)
        db.session.commit()
    return redirect(url_for('vacinadoroute.vacinado'))


@vacinadoroute.route('/vacinado/editar/<string:cns>')
def vacinado_editar(cns):
    vacinado = Vacinado.query.filter_by(cns=cns).first()
    return render_template('vacinado/vacinado_editar.html', titulo='Editando Vacinado', vacinado=vacinado)


@vacinadoroute.route('/excluir/<string:cns>')
def vacinado_excluir(cns):
    try:
        vacinado = Vacinado.query.filter_by(cns=cns).first()
        db.session.delete(vacinado)
        db.session.commit()
        flash(f'O  Vacinado {cns} foi deletado com sucesso!', 'alert-success')
    except KeyError as key:
        raise ValueError(key)

    return redirect(url_for('vacinadoroute.vacinado'))
