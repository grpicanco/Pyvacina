import sqlite3
from datetime import date, datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from DAO.daoVacinador import VacinadorDao
from DAO.daoVacinado import VacinadoDao
from DAO.daoVacina import VacinaDao
from model import Vacinado, Vacinador, Vacina
import re

app = Flask(__name__)
app.config.from_pyfile('config.py')
FILE = "Pyvacina.db"

db = sqlite3.connect(FILE, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES, check_same_thread=False)
vacinado_dao = VacinadoDao(db)
vacinador_dao = VacinadorDao(db)
vacina_dao = VacinaDao(db)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vacinado')
def vacinado():
    lista = vacinado_dao.listar()
    return render_template('vacinado_lista.html', titulo='Vacinados', vacinados=lista)


@app.route('/vacinado/novo')
def vacinado_novo():
    return render_template('vacinado_novo.html', titulo='Novo Vacinado')


@app.route('/criarVacinado', methods=['POST', ])
def vacinado_criar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    cns = request.form['cns']
    dtnascimento = datetime.strptime(request.form['nascimento'], '%Y-%m-%d').date()
    comorbidade = eval(request.form['comorbidade'])
    qtdDose = int(request.form['dose'])
    vacinado = Vacinado(nome=nome, cpf=cpf, cns=cns, dtNascimento=dtnascimento, comorbidade=comorbidade,
                        qtdDose=qtdDose)
    vacinado_dao.salvar(vacinado)
    return redirect(url_for('vacinado'))


@app.route('/vacinado/atualizar/<string:cns>', methods=['POST', ])
def vacinado_atualizar(cns):
    nome = request.form['nome']
    cpf = request.form['cpf']
    dtnascimento = datetime.strptime(request.form['nascimento'], '%Y-%m-%d').date()
    comorbidade = eval(request.form['comorbidade'])
    qtdDose = int(request.form['dose'])
    vacinado = Vacinado(nome=nome, cpf=cpf, cns=cns, dtNascimento=dtnascimento, comorbidade=comorbidade,
                        qtdDose=qtdDose)
    vacinado_dao.salvar(vacinado)
    return redirect(url_for('vacinado'))


@app.route('/vacinado/editar/<string:cns>')
def vacinado_editar(cns):
    vacinado = vacinado_dao.busca_por_cns(cns)
    return render_template('vacinado_editar.html', titulo='Editando Vacinado', vacinado=vacinado)


@app.route('/excluir/<string:cns>')
def vacinado_excluir(cns):
    vacinado_dao.deletar(cns)
    flash(f'O Vacinado {cns} foi deletado com sucesso!')
    return redirect(url_for('vacinado'))


@app.route('/vacinador')
def vacinador():
    lista = vacinador_dao.listar()
    for vacinador in lista:
        vacinador.crmtemplate = vacinador.crm
    return render_template('vacinador_lista.html', titulo="Lista de vacinadores", vacinadores=lista)


@app.route('/vacinador/novo')
def vacinador_novo():
    return render_template("vacinador_novo.html", titulo="Novo vacinador")


@app.route('/vacinador/criar', methods=['POST', ])
def vacinador_criar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    crm = add_crm_banco(request.form['crm'])
    dt_nascimento = datetime.strptime(request.form['nascimento'], '%Y-%m-%d').date()

    vacinador = Vacinador(nome=nome, cpf=cpf, crm=crm, dtNascimento=dt_nascimento)
    vacinador_dao.salvar(vacinador)
    return redirect(url_for('vacinador'))


@app.route('/vacinador/atualizar/<string:crm>', methods=['POST', ])
def vacinador_atualizar(crm):
    nome = request.form['nome']
    cpf = request.form['cpf']
    dt_nascimento = datetime.strptime(request.form['nascimento'], '%Y-%m-%d').date()

    vacinador = Vacinador(nome=nome, cpf=cpf, crm=crm, dtNascimento=dt_nascimento)
    vacinador_dao.salvar(vacinador)
    return redirect(url_for('vacinador'))


def add_crm_banco(param: str) -> str:
    param = param.upper()
    param = re.sub(r"\s+", "", param)
    crm = re.search("([A-Z]{3})(/)([A-Z]{2})([0-9]{6})", param)
    crm = crm.group(1) + crm.group(3) + crm.group(4)
    return crm


@app.route('/vacinador/editar/<string:crm>')
def vacinador_editar(crm):
    vacinador = vacinador_dao.busca_por_crm(crm)
    vacinador.crmtemplate = vacinador.crm
    return render_template("vacinador_editar.html", titulo="Editando Vacinador", vacinador=vacinador)


@app.route('/vacinador/excluir/<string:crm>')
def vacinador_excluir(crm):
    vacinador_dao.deletar(crm)
    return redirect(url_for('vacinador'))


@app.route('/vacina')
def vacina():
    lista = vacina_dao.listar()
    return render_template("vacina_lista.html", titulo="Lista de Vacinas", vacinas=lista)


@app.route('/vacina/novo')
def vacina_novo():
    return render_template("vacina_novo.html", titulo="Nova Vacina.")


@app.route('/vacina/criar', methods=['POST', ])
def vacina_criar():
    nome = request.form['nome']
    vacina = Vacina(nome=nome)
    vacina_dao.salvar(vacina)
    return redirect(url_for('vacina'))


@app.route('/vacina/editar/<int:id>')
def vacina_editar(id):
    vacina = vacina_dao.busca_por_id(id)
    return render_template("vacina_editar.html", vacina=vacina)


@app.route('/vacina/atualiza/<int:id>', methods=['POST', ])
def vacina_atualizar(id):
    nome = request.form['nome']
    vacina = Vacina(nome=nome, id=id)
    vacina_dao.salvar(vacina)
    return redirect(url_for("vacina"))


@app.route('/vacina/excluir/<int:id>')
def vacina_excluir(id):
    vacina_dao.deletar(id)
    return redirect(url_for('vacina'))


app.run(debug=True)
