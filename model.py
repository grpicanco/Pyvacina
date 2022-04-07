import time
from datetime import datetime, date
import re
from enum import property


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
    def __init__(self, nome, cpf, crm, dtNascimento, template=None):
        self.__nome = nome
        self.__cpf = cpf
        self.__crm = crm
        self.__dtNasciento = dtNascimento
        self.__crmtemplate = template

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

    @property
    def crmtemplate(self) -> str:
        return self.__crmtemplate

    @crmtemplate.setter
    def crmtemplate(self, param):
        txt = re.search("([A-Z|a-z]{3})([A-Z|a-z]{2})([0-9]{6})", param)
        txt = f"{txt.group(1)}/{txt.group(2)} {txt.group(3)}"
        self.__crmtemplate = txt


class Vacina:
    def __init__(self, nome, id=None):
        self.__nome = nome
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, param):
        self.__id = param

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, param):
        self.__nome = param


class Aplicacao:
    def __init__(self, cns, crm, id_vacina, id= None, nome_cns=None, nome_crm=None, nome_vacina=None):
        self.__id = id
        self.__cns = cns
        self.__crm = crm
        self.__id_vacina = id_vacina
        self.nome_cns = nome_cns
        self.nome_crm = nome_crm
        self.nome_vacina = nome_vacina

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def cns(self):
        return self.__cns

    @cns.setter
    def cns(self, value):
        self.__cns = value

    @property
    def crm(self):
        return self.__crm

    @crm.setter
    def crm(self, values):
        self.__crm = values

    @property
    def id_vacina(self):
        return self.__id_vacina

    @id_vacina.setter
    def id_vacina(self, values):
        self.__id_vacina = values
