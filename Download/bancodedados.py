from arquivo import *
import sqlite3
from time import sleep
from validate_docbr import *
import colorama
from colorama import Fore, Style
colorama.init()
import os

def lercontratos(x):
    os.system('cls')
    conn = sqlite3.connect('dbalugueisv2.db')
    cursor = conn.cursor()
    if x == False:
        cursor.execute("select contratos.id, inquilinos.nome, imoveis.ref, imoveis.endereço, contratos.valor, contratos.data, contratos.indice from contratos join inquilinos on contratos.idinquilinos = inquilinos.id join imoveis on contratos.idimoveis = imoveis.id order by nome;")
    else:
        cursor.execute(f"select contratos.id, inquilinos.nome, imoveis.ref, imoveis.endereço, contratos.valor, contratos.data, contratos.indice from contratos join inquilinos on contratos.idinquilinos = inquilinos.id join imoveis on contratos.idimoveis = imoveis.id where contratos.id= {x};")

    resultados = cursor.fetchall()
    print()
    print(linhas(147))
    print('{:<3} {:<33} {:<24} {:<45} {:<13} {:<12} {:<5} '.format('ID','INQUILINO', 'CIDADE', 'ENDEREÇO','VALOR','DATA BASE','INDICE'))
    print(linhas(147))
    for linha in resultados:
        print("{:<3} {:<33} {:<24} {:<45} R$ {:<10} {:<13}{:<2} ".format(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6]))
    conn.close()
    print(linhas(147))
    print()


def lerimoveis(x):
    os.system('cls')
    conn = sqlite3.connect('dbalugueisv2.db')
    cursor = conn.cursor()
    if x == False:
        cursor.execute("select * from imoveis order by ref")
    else:
        cursor.execute(f"select * from imoveis where id = {x}")
    resultados = cursor.fetchall()
    print()
    print(linhas(115))
    print('{:<5} {:<30} {}'.format('ID','CIDADE/ESTADO','ENDEREÇO'))
    print(linhas(115))
    for linha in resultados:
        print("{:<5} {:<30} {}".format(linha[0], linha[1], linha[2]))
    conn.close()
    print(linhas(115))
    print()


def lerinquilinos(x):
    os.system('cls')
    conn = sqlite3.connect('dbalugueisv2.db')
    cursor = conn.cursor()
    if x == False:
        cursor.execute("select * from inquilinos order by nome")
    else:
        cursor.execute(f"select * from inquilinos where id = {x}")
    resultados=cursor.fetchall()
    print()
    print(linhas(75))
    print('{:<5} {:<48} {}'.format('ID','NOME','CPF/CNPJ'))
    print(linhas(75))
    for linha in resultados:
        print("{:<5} {:<48} {}".format(linha[0], linha[1], linha[2]))
    conn.close()
    print(linhas(75))
    print()



def cadastrarcontratos(nome, imovel, valor, data, indice):
    conn = sqlite3.connect('dbalugueisv2.db')
    cursor = conn.cursor()
    sql = "INSERT INTO contratos(idinquilinos, idimoveis, valor, data, indice) VALUES (?, ?, ?, ?, ?)"
    val = (nome, imovel, valor, data, indice)
    cursor.execute(sql, val)
    conn.commit()
    print()
    print(f"{Fore.RED}Registro inserido!{Style.RESET_ALL}")
    print()
    sleep(0.5)
    conn.close()
    os.system('cls')


def cadastrarimoveis(ref, endereco):
    conn = sqlite3.connect('dbalugueisv2.db')
    cursor = conn.cursor()
    sql = "INSERT INTO imoveis (ref, endereço) VALUES (?, ?)"
    val = (ref, endereco)
    cursor.execute(sql, val)
    conn.commit()
    print()
    print(f"{Fore.RED}Registro inserido!{Style.RESET_ALL}")
    print()
    sleep(0.5)
    conn.close()
    os.system('cls')


def cadastrarinquilinos(nome, cpf):
    conn = sqlite3.connect('dbalugueisv2.db')
    cursor = conn.cursor()
    sql = "INSERT INTO inquilinos (nome, cpf) VALUES (?, ?)"
    val = (nome, cpf)
    cursor.execute(sql, val)
    conn.commit()
    print()
    print(f"{Fore.RED}Registro inserido!{Style.RESET_ALL}")
    print()
    sleep(0.5)
    conn.close()
    os.system('cls')


def deletar(x,y):
    conn = sqlite3.connect('dbalugueisv2.db')
    cursor = conn.cursor()
    valor = (x,)
    cursor.execute(f"delete from {y} where id = ?",valor)
    conn.commit()
    print()
    print(f"{Fore.RED}Registro apagado!{Style.RESET_ALL}".format(cursor.rowcount))
    print()
    sleep(0.5)
    conn.close()
    os.system('cls')

def editar(x,y,z,t):
    conn = sqlite3.connect('dbalugueisv2.db')
    cursor = conn.cursor()
    valor = (x,)
    cursor.execute(f"update {y} set {t} = '{z}' where id = ?",valor)
    conn.commit()
    print()
    print(f"{Fore.RED}Registro editado!{Style.RESET_ALL}".format(cursor.rowcount))
    print()
    sleep(0.5)
    conn.close()


def validardoc(x):
    conn = sqlite3.connect('dbalugueisv2.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inquilinos WHERE cpf = ?", (x,))
    result = cursor.fetchone()
    if result:
        return False
    else:
        cpf = CPF()
        cpf_valido = cpf.validate(x)
        cnpj = CNPJ()
        cnpj_valido = cnpj.validate(x)

        if cpf_valido:
            return True
        elif cnpj_valido:
            return True


def verifica_se_existe(x,y,z):
    conn = sqlite3.connect('dbalugueisv2.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {y} WHERE {z} = ?", (x,))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False


def verifica_ide_existe(x,y):
    conn = sqlite3.connect('dbalugueisv2.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {y} WHERE id = ?", (x,))
    result = cursor.fetchone()
    if result:
        return False
    else:
        return True

