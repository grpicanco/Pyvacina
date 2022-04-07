import time
from datetime import datetime, date


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
    def dtNascimento(self, param: datetime):
        self.__dtNasciento = param

    @property
    def comorbidade(self) -> bool:
        return self.__comorbidade

    @comorbidade.setter
    def comorbidade(self, param: bool):
        self.__comorbidade = param

    @property
    def qtdDose(self) -> int:
        return self.__qtdDose

    @qtdDose.setter
    def qtdDose(self, param: int):
        self.__qtdDose = param


class Vacinador:
    def __init__(self, nome, cpf, crm, dtNascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__crm = crm
        self.__dtNasciento = dtNascimento


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
    def crm(self) -> str:
        return self.__crm

    @crm.setter
    def crm(self, param: str):
        self.__crm = param

    @property
    def dtNascimento(self) -> datetime:
        return self.__dtNasciento

    @dtNascimento.setter
    def dtNascimento(self, param: datetime):
        self.__dtNasciento = param

