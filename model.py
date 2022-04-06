from datetime import datetime


class Vacinado:
    def __init__(self, nome, cpf, cns, dtNascimento, comorbidade, qtdDose):
        self.__nome = nome
        self.__cpf = cpf
        self.__cns = cns
        self.__dtNasciento = dtNascimento
        self.__comorbidade = comorbidade
        self.__qtdDose = qtdDose

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, param: str):
        self.__nome = param

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, param: str):
        self.__cpf = param

    @property
    def cns(self) -> str:
        return self.__cns

    @cns.setter
    def cns(self, param: str):
        self.__cns = param

    @property
    def dtNascimento(self) -> datetime:
        return self.__dtNasciento

    @dtNascimento.setter
    def dtNascimento(self, param: str):
        self.__dtNasciento = param

    @property
    def comorbidade(self) -> bool:
        return self.__comorbidade

    @comorbidade.setter
    def comorbidade(self, param: str):
        self.__comorbidade = param
    @property
    def qtdDose(self) -> bool:
        return self.__qtdDose

    @qtdDose.setter
    def qtdDose(self, param: str):
        self.__qtdDose = param

