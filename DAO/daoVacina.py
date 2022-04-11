from model import Vacina

SQL_DELETA_VACINA = 'delete from vacina where id = ?'
SQL_VACINA_POR_ID = 'SELECT id, nome from vacina where id = ?'
SQL_ATUALIZA_VACINA = 'UPDATE vacina SET id=?, nome=? where id = ?'
SQL_BUSCA_VACINAS = 'SELECT id, nome from vacina'
SQL_CRIA_VACINA = 'INSERT into vacina (nome) values (?)'


class VacinaDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, vacina):
        cursor = self.__db.cursor()
        if self.existe(vacina):
            cursor.execute(SQL_ATUALIZA_VACINA, (vacina.id,  vacina.nome, vacina.id))
        else:
            cursor.execute(SQL_CRIA_VACINA, (vacina.nome, ))
        self.__db.commit()
        return vacina

    def listar(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_BUSCA_VACINAS)
        vacinas = traduz_vacinas(cursor.fetchall())
        return vacinas

    def busca_por_id(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_VACINA_POR_ID, (id,))
        tupla = cursor.fetchone()
        if tupla:
            return Vacina(id=tupla[0], nome=tupla[1])
        return False

    def deletar(self, id):
        self.__db.cursor().execute(SQL_DELETA_VACINA, (id, ))
        self.__db.commit()

    def existe(self, vacina):
        if self.busca_por_id(vacina.id):
            return True
        return False


def traduz_vacinas(vacinadores):
    def cria_vacinas_com_tupla(tupla):
        return Vacina(id=tupla[0], nome=tupla[1])
    return list(map(cria_vacinas_com_tupla, vacinadores))
