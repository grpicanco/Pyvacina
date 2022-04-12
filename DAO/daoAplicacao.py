from model import Aplicacao

SQL_DELETA_APLICACAO = 'delete from aplicacao where id = ?'
SQL_APLICACAO_POR_ID = "SELECT id, cns, crm, id_vacina, data FROM aplicacao a where a.id = ?;"
SQL_ATUALIZA_APLICACAO = 'UPDATE aplicacao SET id=?, cns=?, crm=?, id_vacina=?, data=? where id = ?'
SQL_BUSCA_APLICACAO = 'SELECT id, cns, crm, id_vacina, data FROM aplicacao;'
SQL_CRIA_APLICACAO = 'INSERT into aplicacao (cns,crm, id_vacina, data) values (?, ?, ?, ?);'
SQL_UPDATE_QTDOSE = "update vacinado set qtdDose = (select count(a.cns) from aplicacao a where a.cns = ? group by a.cns) where vacinado.cns = ?;"


class AplicacaoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, aplicacao):
        cursor = self.__db.cursor()
        if self.existe(aplicacao):
            cursor.execute(SQL_ATUALIZA_APLICACAO, (
                aplicacao.id, aplicacao.cns, aplicacao.crm, aplicacao.id_vacina, aplicacao.dtaplicacao, aplicacao.id))
            cursor.execute(SQL_UPDATE_QTDOSE, (aplicacao.cns, aplicacao.cns))
        else:
            cursor.execute(SQL_CRIA_APLICACAO,
                           (aplicacao.cns, aplicacao.crm, aplicacao.id_vacina, aplicacao.dtaplicacao))
            cursor.execute(SQL_UPDATE_QTDOSE, (aplicacao.cns, aplicacao.cns))
        self.__db.commit()
        return aplicacao

    def listar(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_BUSCA_APLICACAO)
        aplicacao = traduz_aplicacao(cursor.fetchall())
        return aplicacao

    def busca_por_id(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_APLICACAO_POR_ID, (id,))
        tupla = cursor.fetchone()
        if tupla:
            return Aplicacao(id=tupla[0], cns=tupla[1], crm=tupla[2], id_vacina=tupla[3], data=tupla[4])
        return False

    def deletar(self, id):
        self.__db.cursor().execute(SQL_DELETA_APLICACAO, (id,))
        self.__db.commit()

    def existe(self, aplicacao):
        if self.busca_por_id(aplicacao.id):
            return True
        return False


def traduz_aplicacao(aplicacao):
    def cria_aplicacao_com_tupla(tupla):
        return Aplicacao(id=tupla[0], cns=tupla[1], crm=tupla[2],
                         id_vacina=tupla[3], data=tupla[4])

    return list(map(cria_aplicacao_com_tupla, aplicacao))
