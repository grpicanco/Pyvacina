import sqlite3 as sql

conn = sql.connect('../Pyvacina.db')

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS vacinado")

sql = '''
CREATE TABLE "vacinado"(
    "cns" VARCHAR(15) PRIMARY KEY, 
    "cpf" VARCHAR(11) NOT NULL UNIQUE,
    "nome" VARCHAR(128) NOT NULL,
    "dtNascimento" DATE NOT NULL, 
    "comorbidade" INTEGER, 
    "qtdDose" INTEGER
);
'''

cur.execute(sql)
print('create table vacinado')

cur.execute("DROP TABLE IF EXISTS vacinador")

sql = '''
CREATE TABLE "vacinador"(
    "crm" VARCHAR(13) PRIMARY KEY, 
    "cpf" VARCHAR(11) NOT NULL UNIQUE,
    "nome" VARCHAR(128) NOT NULL,
    "dtNascimento" DATE NOT NULL
      
);
'''

cur.execute(sql)
print('create table vacinador')

cur.execute("DROP TABLE IF EXISTS vacina")

sql = '''
CREATE TABLE "vacina"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "nome" VARCHAR(128) NOT NULL 
);
'''

cur.execute(sql)
print('create table vacina')

cur.execute("DROP TABLE IF EXISTS aplicacao")

sql = '''
CREATE TABLE "aplicacao"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "cns" VARCHAR(15) NOT NULL,
    "crm" VARCHAR(13) NOT NULL,
    "id_vacina" INTEGER NOT NULL,
    "data" DATE,
    FOREIGN KEY (cns) REFERENCES vacinado(cns)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (crm) REFERENCES vacinador(crm)
        ON DELETE RESTRICT 
        ON UPDATE CASCADE,
    FOREIGN KEY (id_vacina) REFERENCES vacina(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
'''


cur.execute(sql)
print('create table aplcacao')



cur.close()
conn.close()
