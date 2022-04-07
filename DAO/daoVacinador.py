from model import Vacinador

SQL_DELETA_VACINADOR = 'delete from vacinador where crm like ?'
SQL_VACINADOR_POR_CRM = 'SELECT crm, cpf, nome, dtNascimento from vacinador where crm like ?'
SQL_ATUALIZA_VACINADOR = 'UPDATE vacinador SET crm=?, cpf=?, nome=?, dtNascimento=? where crm like ?'
SQL_BUSCA_VACINADORES = 'SELECT crm, cpf, nome, dtNascimento from vacinador'
SQL_CRIA_VACINADOR = 'INSERT into vacinador (crm, cpf, nome, dtNascimento) values (?, ?, ?, ?)'


class VacinadorDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, vacinador):
        cursor = self.__db.cursor()
        if self.existe(vacinador):
            cursor.execute(SQL_ATUALIZA_VACINADOR, (vacinador.crm, vacinador.cpf, vacinador.nome, vacinador.dtNascimento, vacinador.crm))
        else:
            cursor.execute(SQL_CRIA_VACINADOR, (vacinador.crm, vacinador.cpf, vacinador.nome, vacinador.dtNascimento))
        self.__db.commit()
        return vacinador

    def listar(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_BUSCA_VACINADORES)
        vacinadores = traduz_vacinadores(cursor.fetchall())
        return vacinadores

    def busca_por_crm(self, crm):
        cursor = self.__db.cursor()
        cursor.execute(SQL_VACINADOR_POR_CRM, (crm,))
        tupla = cursor.fetchone()
        if tupla:
            return Vacinador(crm=tupla[0], cpf=tupla[1], nome=tupla[2], dtNascimento=tupla[3])
        return False

    def deletar(self, crm):
        self.__db.cursor().execute(SQL_DELETA_VACINADOR, (crm, ))
        self.__db.commit()

    def existe(self, vacinador):
        if self.busca_por_crm(vacinador.crm):
            return True
        return False


def traduz_vacinadores(vacinadores):
    def cria_vacinadores_com_tupla(tupla):
        return Vacinador(crm=tupla[0], cpf=tupla[1], nome=tupla[2], dtNascimento=tupla[3])
    return list(map(cria_vacinadores_com_tupla, vacinadores))
