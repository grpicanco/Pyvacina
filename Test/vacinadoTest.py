from datetime import datetime

from models.vacinado import Vacinado


def run(nome, cpf, cns, dtNascimento, comorbidade,
        qtdDose):
    try:
        assert type(nome) == str, f'Nome precisa ser uma String.'
        assert len(nome) <= 124, f'Nome execedeu a quantidade de 124 caracteres.'
        assert len(cpf) == 11, f'CPF invalido.'
        assert Vacinado.query.filter_by(cpf=cpf).first() is None, f'Este CPF: {cpf} ja existe!'
        assert len(cns) == 15, f'CNS invalido.'
        assert Vacinado.query.filter_by(cns=cns).first() is None, f'Este CNS: {cns} ja existe!'
        # assert type(dtNascimento) == datetime.date, f'1Data: {dtNascimento} invalida!'
        assert dtNascimento <= datetime.now().date(), f'2Data: {dtNascimento} invalida!'
        assert type(comorbidade) == bool, f'Erro se apresenta comorbidade!'
        assert type(qtdDose) == int, f'Erro ao cadastrar quantidade de dose'

        return True, Vacinado(nome=nome, cpf=cpf, cns=cns, dtNascimento=dtNascimento, comorbidade=comorbidade,
                              qtdDose=qtdDose)

    except AssertionError as er:
        return False, str(er)


class VacinadoTest:

    def __init__(self, cpf, cns, dtnascimento, comorbidade, qtdDose, nome=None):
        self.value, self.vacinado = run(nome=nome, cpf=cpf, cns=cns, dtNascimento=dtnascimento,
                                    comorbidade=comorbidade, qtdDose=qtdDose)
