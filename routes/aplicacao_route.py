from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for

from extensions import db
from models.aplicacao import Aplicacao
from models.vacina import Vacina
from models.vacinado import Vacinado
from models.vacinador import Vacinador

aplicacaoroute = Blueprint('aplicacaoroute', __name__)


@aplicacaoroute.route('/aplicacao/')
def aplicacao():
    lista = Aplicacao.query.all()
    return render_template('aplicacao/aplicacao_list.html', titulo='Aplicações de Vacinas', aplicacoes=lista)


@aplicacaoroute.route('/aplicacao/novo/')
def aplicacao_novo():
    lista_vacina = Vacina.query.all()
    lista_vacinador = Vacinador.query.all()
    lista_vacinado = Vacinado.query.all()

    for vacinador in lista_vacinador:
        vacinador.crmtemplate = Vacinador.trazer_crm(vacinador.crm)

    return render_template("aplicacao/aplicacao_novo.html", titulo="Nova Aplicacao.", vacinas=lista_vacina,
                           vacinadores=lista_vacinador, vacinados=lista_vacinado)


@aplicacaoroute.route('/aplicacao/criar', methods=['POST', ])
def aplicacao_criar():
    id_vacina = request.form['vacina']
    cns = request.form['vacinado']
    crm = request.form['vacinador']
    data = datetime.now().date()
    aplicacao = Aplicacao(id_vacina=id_vacina, cns=cns, crm=crm, data=data)

    db.session.add(aplicacao)
    db.session.commit()
    att_dose(aplicacao.cns)

    return redirect(url_for('aplicacaoroute.aplicacao'))


@aplicacaoroute.route('/aplicacao/editar/<int:id>')
def aplicacao_editar(id):
    aplicacao = Aplicacao.query.filter_by(id=id).first()
    lista_vacina = Vacina.query.all()
    lista_vacinador = Vacinador.query.all()
    lista_vacinado = Vacinado.query.all()

    for vacinador in lista_vacinador:
        vacinador.crmtemplate = Vacinador.trazer_crm(vacinador.crm)

    return render_template("aplicacao/aplicacao_editar.html", aplicacao=aplicacao, vacinados=lista_vacinado,
                           vacinadores=lista_vacinador, vacinas=lista_vacina)


@aplicacaoroute.route('/aplicacao/atualizar/<int:id>', methods=['POST', ])
def aplicacao_atualizar(id):
    aplicacao = Aplicacao.query.filter_by(id=id)
    aplicacao.id_vacina = request.form['vacina']
    aplicacao.cns = request.form['vacinado']
    aplicacao.crm = request.form['vacinador']
    db.session.commit()
    att_dose(aplicacao.cns)
    return redirect(url_for("aplicacaoroute.aplicacao"))


@aplicacaoroute.route('/aplicacao/excluir/<int:id>', methods=['GET', 'DELETE'])
def aplicacao_excluir(id):
    aplicacao = Aplicacao.query.filter_by(id=id).first()
    cns = aplicacao.cns
    db.session.delete(aplicacao)
    db.session.commit()
    if cns:
        att_dose(cns)
    return redirect(url_for('aplicacaoroute.aplicacao'))


@aplicacaoroute.route('/aplicacao/filtro/', methods=['POST', ])
def aplicacao_filtro():
    cpf = request.form['cpf']
    lista = Aplicacao.query.join(Vacinado).where(Vacinado.cpf == cpf)
    if lista:
        return render_template('aplicacao/aplicacao_list.html', titulo='Aplicações de Vacinas', aplicacoes=lista)
    else:
        return redirect(url_for('aplicacaoroute.aplicacao'))


def att_dose(cns):
    qtd = Aplicacao.query.where(Aplicacao.cns == cns).count()
    vacinado = Vacinado.query.filter_by(cns=cns).first()
    vacinado.qtdDose = qtd
    db.session.commit()
