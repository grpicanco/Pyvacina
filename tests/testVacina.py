from model import Vacina


class vacinaTeste:
    def __init__(self, nome):
        self.run(nome)

    def run(self, nome):
        assert type(nome) == str, "Nome precisar ser uma String."
        assert len(nome) <= 124, "Nome da vacina muito extenso."
        return Vacina(nome)
