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
    if x == False: # SERÁ EXIBIDO NA TELA TODOS OS DADOS DO CONTRATO
        cursor.execute("select contratos.id, inquilinos.nome, imoveis.ref, imoveis.endereço, contratos.valor, contratos.data, contratos.indice from contratos join inquilinos on contratos.idinquilinos = inquilinos.id join imoveis on contratos.idimoveis = imoveis.id order by nome COLLATE NOCASE;")
    else: # SERÁ EXIBIDO NA TELA APENAS OS DADOS REFERENTE O Nº ID SELECIONADO
        cursor.execute(f"select contratos.id, inquilinos.nome, imoveis.ref, imoveis.endereço, contratos.valor, contratos.data, contratos.indice from contratos join inquilinos on contratos.idinquilinos = inquilinos.id join imoveis on contratos.idimoveis = imoveis.id where contratos.id= {x};")
    resultados = cursor.fetchall()
    print()
    print(linhas(147))
    print('{:<3} {:<33} {:<24} {:<43} {:<14} {:<12} {:<5} '.format('ID','INQUILINO', 'CIDADE', 'ENDEREÇO','VALOR','DATA BASE','INDICE'))
    print(linhas(147))
    for linha in resultados:
        print("{:<3} {:<33} {:<24} {:<43} R$ {:<11} {:<13}{:<2} ".format(linha[0], linha[1], linha[2], linha[3], transforma_valor(linha[4]), linha[5], linha[6]))
    conn.close()
    print(linhas(147))
    print()


def TotalAlugueis():
    conn = sqlite3.connect('dbalugueisv2.db')
    cursor = conn.cursor()
    cursor.execute("select contratos.valor from contratos;")
    resultados = cursor.fetchall()
    print()
    print(linhas(100))
    cont = 0
    c=0
    for linha in resultados:
        cont = linha[0] + cont
        c=c+1
    print("Sua recebimento mensal de alugueis está previsto em {}R$ {}{} provenientes de {}{}{} contratos ativos".format(Fore.LIGHTYELLOW_EX,transforma_valor(cont),Style.RESET_ALL,Fore.LIGHTYELLOW_EX,c,Style.RESET_ALL))
    print(linhas(100))
    print()
    conn.close()


def lerimoveis(x):
    os.system('cls')
    conn = sqlite3.connect('dbalugueisv2.db')
    cursor = conn.cursor()
    if x == False:
        cursor.execute("select * from imoveis order by ref COLLATE NOCASE, endereço COLLATE NOCASE ")
    else:
        cursor.execute(f"select * from imoveis where id = {x}")
    resultados = cursor.fetchall()
    print()
    print(linhas(85))
    print('{:<5} {:<30} {}'.format('ID','CIDADE/ESTADO','ENDEREÇO'))
    print(linhas(85))
    for linha in resultados:
        print("{:<5} {:<30} {}".format(linha[0], linha[1], linha[2]))
    conn.close()
    print(linhas(85))
    print()


def lerinquilinos(x):
    os.system('cls')
    conn = sqlite3.connect('dbalugueisv2.db')
    cursor = conn.cursor()
    if x == False:
        cursor.execute("select * from inquilinos order by nome COLLATE NOCASE")
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

