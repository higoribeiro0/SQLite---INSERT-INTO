import sqlite3 
from sqlite3 import Error

###Criar conexao
def ConexaoBanco():
    caminho="D:\\Python\\Banco\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

nome=input("Digite o seu nome: ")
telefone=input("Digite o telefone: ")
email=input("Digite o seu email: ")

vsql="INSERT INTO tb_contatos(T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)VALUES('"+nome+"','"+telefone+"','"+email+"')"

def insert(conexao,sql):
    try: 
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro Inserido")
    except Error as ex:
        print(ex)
