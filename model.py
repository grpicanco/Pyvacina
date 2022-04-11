import time
from datetime import datetime, date
import re

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
    def __init__(self, cns, crm, id_vacina, data, id=None, vacina_nome=None, vacinador_nome=None, vacinado_nome=None, crm_template=None):
        self.__id = id
        self.__cns = cns
        self.__crm = crm
        self.__crm_template = crm_template
        self.__id_vacina = id_vacina
        self.__dtaplicacao = data
        self.__vacina_nome = vacina_nome
        self.__vacinador_nome = vacinador_nome
        self.__vacinado_nome = vacinado_nome

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

    @property
    def dtaplicacao(self):
        return self.__dtaplicacao

    @dtaplicacao.setter
    def dtaplicacao(self, values):
        self.__dtaplicacao = values

    @property
    def vacina_nome(self):
        return self.__vacina_nome

    @vacina_nome.setter
    def vacina_nome(self, values):
        self.__vacina_nome = values

    @property
    def vacinador_nome(self):
        return self.__vacinador_nome

    @vacinador_nome.setter
    def vacinador_nome(self, values):
        self.__vacinador_nome = values

    @property
    def vacinado_nome(self):
        return self.__vacinado_nome

    @vacinado_nome.setter
    def vacinado_nome(self, values):
        self.__vacinado_nome = values

    @property
    def crm_template(self):
        return self.__crm_template

    @crm_template.setter
    def crm_template(self, values):
        self.__crm_template = values

    def __str__(self):
        return str(self.id) + '|' + str(self.id_vacina) + '|' + self.crm + '|' + str(self.cns)