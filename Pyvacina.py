import sqlite3
from datetime import date, datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from DAO.daoVacinador import VacinadorDao
from DAO.daoVacinado import VacinadoDao
from model import Vacinado, Vacinador

app = Flask(__name__)
app.config.from_pyfile('config.py')
FILE = "Pyvacina.db"

db = sqlite3.connect(FILE, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES, check_same_thread=False)
vacinado_dao = VacinadoDao(db)
vacinador_dao = VacinadorDao(db)


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


@app.route('/vacinado/editar/<string:cns>')
def vacinado_editar(cns):
    vacinado = vacinado_dao.busca_por_cns(cns)
    return render_template('vacinado_editar.html', titulo='Editando Vacinado', vacinado=vacinado)


@app.route('/atualizar', methods=['POST', ])
def vacinado_atualizaar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    cns = request.form['cns']
    dtnascimento = date(request.form['nascimento'])
    comorbidade = bool(request.form['comorbidade'])
    qtdDose = int(request.form['dose'])
    vacinado = Vacinado(nome=nome, cpf=cpf, cns=cns, dtNascimento=dtnascimento, comorbidade=comorbidade,
                        qtdDose=qtdDose)
    vacinado_dao.salvar(vacinado)
    return redirect(url_for('vacinado'))


@app.route('/excluir/<string:cns>')
def vacinado_excluir(cns):
    vacinado_dao.deletar(cns)
    flash(f'O Vacinado {cns} foi deletado com sucesso!')
    return redirect(url_for('vacinado'))


@app.route('/vacinador')
def vacinador():
    lista = vacinador_dao.listar()
    return render_template('vacinador_list.html', titulo="Lista de vacinadores", vacinadores=lista)

@app.route('/vacinador/novo')
def vacinador_novo():
    return render_template("vacinador_novo.html", titulo="Novo vacinador")

@app.route('/vacinador/criar', methods=['POST', ])
def vacinador_criar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    crm = request.form['crm']
    dt_nascimento = request.form['nascimento']
    vacinador = Vacinador(nome=nome, cpf=cpf, crm=crm, dtNascimento=dt_nascimento)
    vacinador_dao.salvar(vacinador)
    return redirect(url_for('vacinador'))

@app.route('/vacinador/editar/<string:crm>')
def vacinador_editar(crm):
    pass

@app.route('/vacinador/excluir/<string:crm>')
def vacinador_excluir(crm):
    pass


app.run(debug=True)
