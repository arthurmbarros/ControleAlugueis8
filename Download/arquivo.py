import datetime
from time import sleep
import colorama
from colorama import Fore, Style
colorama.init()

def leiadinheiro(msg):
    while True:
        valor = str(input(msg)).replace(',', '.').strip()
        if valor.strip().lower() == 'exit':
            return valor
        else:
            try:
                valor_float = float(valor)
            except ValueError:
                print(f'{Fore.RED}ERRO: \"{valor}\" é um preço inválido!{Style.RESET_ALL}')
            else:
                break
    return valor_float


def validar_data(data_str): #Obriga o usuário do sistema a inserir data no padrão: dd/mm/aaaa
    try:
        datetime.datetime.strptime(data_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f"{Fore.RED}ERRO: Por favor, digite um número inteiro válido.{Style.RESET_ALL}")
            continue
        except (KeyboardInterrupt):
            print(f"{Fore.RED}Usuário preferiu não digitar esse número.{Style.RESET_ALL}")
            return 0
        else:
            return n
def linhas(tam):
    return '-' * tam

def cabeçalho(txt,tam):
    print(linhas(tam))
    print(txt.center(tam))
    print(linhas(tam))

# título: O que seráa escrito no cabeçalho do MENU.
# linha: Quantidade de caracteres '-' que será colocado  no corpo do MENU.
# lista: Dados do MENU
def menu(titulo, tam, lista):
    cabeçalho(titulo,tam)
    c = 1
    for item in lista:
        print(f'{Fore.YELLOW}{c}{Fore.LIGHTCYAN_EX} - {item}{Style.RESET_ALL}')
        c += 1
    print(linhas(tam))
    opc = leiaInt(f'{Fore.GREEN}Sua opção: {Style.RESET_ALL}')
    return opc


def exit_():
    linhas(32)
    print(f'{Fore.YELLOW}Digite a palavra "exit" para cancelar{Style.RESET_ALL}')
    linhas(32)
    print()
    sleep(1)

def exibir_tela_inicial():

    print(f"{Fore.LIGHTCYAN_EX}*********************************")
    print("*       SISTEMA DE GESTÃO       *")
    print("*                               *")
    print("*      CONTRATOS DE LOCAÇÃO     *")
    print("*                               *")
    print("*         Versão 7.0            *")
    print("*                               *")
    print("*********************************")
    print(f"{Style.RESET_ALL}")
    print("Iniciando...")
    print()
    sleep(3)
    print(f"{Fore.LIGHTCYAN_EX}Inicialização concluída!{Style.RESET_ALL}")