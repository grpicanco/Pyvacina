from model import Vacinado

SQL_DELETA_VACINADO = 'delete from vacinado where cns = ?'
SQL_VACINADO_POR_CNS = 'SELECT cns, cpf, nome, dtNascimento, comorbidade, qtdDose from vacinado where cns = ?'
SQL_ATUALIZA_VACINADO = 'UPDATE vacinado SET cns=?, cpf=?, nome=?, dtNascimento=?, comorbidade=?, qtdDose=? where cns = ?'
SQL_BUSCA_VACINADOS = 'SELECT cns, cpf, nome, dtNascimento, comorbidade, qtdDose from vacinado'
SQL_CRIA_VACINADO = 'INSERT into vacinado (cns, cpf, nome, dtNascimento, comorbidade, qtdDose) values (?, ?, ?, ?, ?, ?)'


class VacinadoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, vacinado):
        cursor = self.__db.cursor()
        if self.existe(vacinado):
            cursor.execute(SQL_ATUALIZA_VACINADO, (vacinado.cns, vacinado.cpf, vacinado.nome, vacinado.dtNascimento, vacinado.comorbidade, vacinado.qtdDose, vacinado.cns))
        else:
            cursor.execute(SQL_CRIA_VACINADO, (vacinado.cns, vacinado.cpf, vacinado.nome, vacinado.dtNascimento, vacinado.comorbidade, vacinado.qtdDose))
        self.__db.commit()
        return vacinado

    def listar(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_BUSCA_VACINADOS)
        vacinados = traduz_vacinados(cursor.fetchall())
        return vacinados

    def busca_por_cns(self, cns):
        cursor = self.__db.cursor()
        cursor.execute(SQL_VACINADO_POR_CNS, (cns,))
        tupla = cursor.fetchone()
        if tupla:
            return Vacinado(cns=tupla[0], cpf=tupla[1], nome=tupla[2], dtNascimento=tupla[3], comorbidade=tupla[4], qtdDose=tupla[5])
        return False

    def deletar(self, cns):
        self.__db.cursor().execute(SQL_DELETA_VACINADO, (cns, ))
        self.__db.commit()

    def existe(self, vacinado):
        if self.busca_por_cns(vacinado.cns):
            return True
        return False


def traduz_vacinados(vacinados):
    def cria_vacinados_com_tupla(tupla):
        return Vacinado(cns=tupla[0], cpf=tupla[1], nome=tupla[2], dtNascimento=tupla[3], comorbidade=tupla[4], qtdDose=tupla[5])
    return list(map(cria_vacinados_com_tupla, vacinados))
