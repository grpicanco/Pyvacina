from datetime import date

from flask import Flask, render_template, request, redirect, session, flash, url_for
from model import Vacinado

app = Flask(__name__)
app.secret_key = 'Pyvacina123'

vacinado1 = Vacinado(nome='Gabriel Picanço', cpf='02646246293', cns='02646246293', dtNascimento=date(1996, 7, 14),
                     comorbidade=False, qtdDose=1)
vacinado2 = Vacinado(nome='James Thomas', cpf='02646246294', cns='02646246293', dtNascimento=date(1996, 7, 14),
                     comorbidade=False, qtdDose=1)
lista = [vacinado1, vacinado2]


@app.route('/')
def index():
    return render_template('inicio.html', titulo='Vacinados', vacinados=lista)


@app.route('/novo')
def novo():
    return render_template('NovoVacinado.html', titulo='Novo Vacinado')


@app.route('/criarVacinado', methods=['POST', ])
def criar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    cns = request.form['cns']
    dtnascimento = request.form['nascimento']
    comorbidade = request.form['comorbidade']
    qtdDose = request.form['dose']

    vacinado = Vacinado(nome=nome, cpf=cpf, cns=cns, dtNascimento=dtnascimento, comorbidade=comorbidade,
                        qtdDose=qtdDose)
    lista.append(vacinado)
    flash(f"Vacinado {vacinado.nome} cadastrado com Sucesso!")
    return redirect(url_for('index'))


app.run(debug=True)

