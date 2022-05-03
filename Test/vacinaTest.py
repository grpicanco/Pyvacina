def run(nome):
    try:
        assert type(eval(nome)) == str, f'Campo nome deve ser uma string'
        assert len(nome) <= 124, f'Campo nome deve ser menor que 124 caracteres'

        return True, str(nome)
    except AssertionError as er:
        return False, str(er)


class VacinaTest:

    def __init__(self, nome):
        self.value, self.text = run(nome=nome)
