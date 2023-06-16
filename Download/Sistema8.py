from bancodedados import *
val=False
import colorama
from colorama import Fore, Style
colorama.init()
def menuprincipal():
    while True:
        os.system('cls')
        resposta = menu('MENU PRINCIPAL',30,['Contratos', 'Imóveis', 'Inquilinos', 'Sair do sistema'])
        if resposta == 1: #CONTRATOS
            contratos()
        elif resposta == 2: # IMÓVEIS
            imoveis()
        elif resposta == 3: # INQUILINOS
            inquilinos()
        elif resposta == 4:  # SAIR DO SISTEMA
            sair()
        else:
            print()
            print(f"{Fore.RED}ERRO! Digite uma opção válida!{Style.RESET_ALL}")


def contratos():
    os.system('cls')
    while True:
        resposta = menu('CONTRATOS', 30,
                        ['Cadastrar novo contrato', 'Ver contratos cadastrados', 'Editar registro', 'Apagar registro',
                         'Menu anterior', 'Sair do sistema'])
        if resposta == 1:  # CADASTRAR NOVO CONTRATO
            cadastrar_contratos()
        elif resposta == 2:  # VER CONTRATOS CADASTRADOS
            lercontratos(val)
            sleep(1)
        elif resposta == 3:  # EDITAR CONTRATOS
            editar_contratos()
        elif resposta == 4:  # APAGAR CONTRATOS
            apagar_contratos()
        elif resposta == 5: # MENU PRINCIPAL
            menuprincipal()
        elif resposta == 6: # SAIR
            sair()
        else:
            print()
            print(f"{Fore.RED}ERRO! Digite uma opção válida!{Style.RESET_ALL}")


def cadastrar_contratos():
    os.system('cls')
    lerinquilinos(val)
    exit_()
    inquilino = input('Digite o ID do inquilino que deseja cadastrar no contrato: ').strip()
    if inquilino.lower().strip() == 'exit':
        contratos()
    while inquilino == '' or inquilino.isalpha() or verifica_ide_existe(inquilino, 'inquilinos'):
        print(f"{Fore.RED}ID inválido, digite novamente: {Style.RESET_ALL}")
        inquilino = input('Digite o ID do inquilino que deseja cadastrar no contrato: ')
        if inquilino.lower().strip() == 'exit':
            contratos()
    lerimoveis(val)
    imovel = input('Digite o ID do imóvel que deseja cadastrar no contrato: ').strip()
    if imovel.lower().strip() == 'exit':
        contratos()
    while imovel == '' or verifica_se_existe(imovel, 'contratos', 'idimoveis') or verifica_ide_existe(imovel,
                                                                                                      'imoveis') or imovel.isalpha():
        if verifica_se_existe(imovel, 'contratos', 'idimoveis'):
            print("\033[31mImovel já está em um contrato ativo. Selecione outro imóvel:\033[0m")
        else:
            print("\033[31mID inválido, digite novamente:\033[0m")
        imovel = input('Digite o ID do imóvel que deseja cadastrar no contrato: ')
        if imovel.lower().strip() == 'exit':

            contratos()
    aluguel = leiadinheiro('Digite o valor do aluguel: R$ ')
    if aluguel == 'exit':
        contratos()
    data = input('Digite a data de assinatura do contrato (dd/mm/aaaa): ')
    if data.lower().strip() == 'exit':
        os.system('cls')
        contratos()
    while not validar_data(data):
        print(f"{Fore.RED}Data inválida. Digite novamente.{Style.RESET_ALL}")
        data = input("Digite a data de assinatura do contrato (dd/mm/aaaa): ")
        if data.lower().strip() == 'exit':
            os.system('cls')
            contratos()
    while True:
        indice = input('Digite o índice de reajuste (enter se for IGPM): ').strip().upper()
        if len(indice) > 10:
            print()
            print(f"{Fore.RED}Você digitou {len(indice)} caracteres, favor abreviar para no maximo 10.{Style.RESET_ALL}")
            print()
            sleep(0.5)
        else:
            break
    if indice.lower().strip() == 'exit':
        contratos()
    elif indice == '':
        indice = 'IGPM'
    cadastrarcontratos(inquilino, imovel, aluguel, data, indice)

def editar_contratos():
    os.system('cls')
    lercontratos(val)
    exit_()
    x = input('Digite o número ID do contrato que deseja editar: ')
    if x.lower().strip() == 'exit':
        os.system('cls')
        contratos()
    while verifica_ide_existe(x, 'contratos') or x == '' or x.isalpha():
        print("\033[31m""ID inválido ou está em um contrato ativo, digite novamente:""\033[0m")
        x = input('Digite o número ID do imóvel que deseja editar: ')
        if x.lower().strip() == 'exit':
            os.system('cls')
            contratos()
    while True:
        resposta = menu('DIGITE O Nº QUE DESEJA EDITAR', 30,['Inquilinos', 'Imóveis', 'Valor do aluguel', 'Data', 'Indice', 'Menu anterior','Sair do sistema'])
        if resposta == 1:
            lerinquilinos(val)
            inquilino = input('Digite o ID do inquilino que deseja editar no contrato: ').strip()
            if inquilino.lower().strip() == 'exit':
                os.system('cls')
                contratos()
            while inquilino == '' or inquilino.isalpha() or verifica_ide_existe(inquilino, 'inquilinos'):
                print(f"{Fore.RED}ID inválido, digite novamente: {Style.RESET_ALL}")
                inquilino = input('Digite o ID do imóvel que deseja cadastrar no contrato: ')
                if inquilino.lower().strip() == 'exit':
                    os.system('cls')
                    contratos()
            editar(x, 'contratos', inquilino, 'idinquilinos')
            lercontratos(x)

        elif resposta == 2:
            os.system('cls')
            lerimoveis(val)
            imovel = input('Digite o ID do imóvel que deseja cadastrar no contrato: ').strip()
            if imovel.lower().strip() == 'exit':
                os.system('cls')
                contratos()
            while imovel == '' or verifica_se_existe(imovel, 'contratos', 'idimoveis') or verifica_ide_existe(
                    imovel, 'imoveis') or imovel.isalpha():
                if verifica_se_existe(imovel, 'contratos', 'idimoveis'):
                    print(f"{Fore.RED}Imovel já está em um contrato ativo. Selecione outro imóvel: {Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}ID inválido, digite novamente: {Style.RESET_ALL}")
                imovel = input('Digite o ID do imóvel que deseja cadastrar no contrato: ')
                if imovel.lower().strip() == 'exit':
                    os.system('cls')
                    contratos()
            editar(x, 'contratos', imovel, 'idimoveis')
            lercontratos(x)

        elif resposta == 3:
            aluguel = leiadinheiro('Digite o novo valor do aluguel: R$ ')
            if aluguel == 'exit':
                os.system('cls')
                contratos()
            editar(x, 'contratos', aluguel, 'valor')
            lercontratos(x)

        elif resposta == 4:
            os.system('cls')
            data = input('Digite uma nova data de assinatura do contrato (dd/mm/aaaa): ')
            if data.lower().strip() == 'exit':
                os.system('cls')
                contratos()
            while not validar_data(data):
                print(f"{Fore.RED}Data inválida! Digite novamente.{Style.RESET_ALL}")
                data = input("Digite a data de assinatura do contrato (dd/mm/aaaa): ")
                if data.lower().strip() == 'exit':
                    os.system('cls')
                    contratos()
            editar(x, 'contratos', data, 'data')
            lercontratos(x)

        elif resposta == 5:
            os.system('cls')
            while True:
                indice = input('Digite o índice de reajuste (enter se for IGPM): ').strip().upper()
                if len(indice) > 10:
                    print()
                    print(f"{Fore.RED}Você digitou {len(indice)} caracteres, favor abreviar para no maximo 10.{Style.RESET_ALL}")
                    print()
                    sleep(0.5)
                else:
                    break
            if indice.lower().strip() == 'exit':
                os.system('cls')
                contratos()
            elif indice == '':
                indice = 'IGPM'
            editar(x, 'contratos', indice, 'indice')
            lercontratos(x)
        elif resposta == 6:
            os.system('cls')
            contratos()
        elif resposta == 7:
            os.system('cls')
            sair()
        else:
            print()
            print(f"{Fore.RED}ERRO! Digite uma opção válida!{Style.RESET_ALL}")
def apagar_contratos():
    os.system('cls')
    lercontratos(val)
    exit_()
    x = input('Digite o número ID do contrato que deseja apagar: ')
    if x.lower().strip() == 'exit':
        os.system('cls')
        contratos()
    while verifica_ide_existe(x, 'contratos') or x == '' or x.isalpha():
        print(f"{Fore.RED}ID inválido, digite novamente:{Style.RESET_ALL}")
        x = input('Digite o número ID do contrato que deseja apagar: ')
        if x.lower().strip() == 'exit':
            os.system('cls')
            contratos()
    deletar(x, 'contratos')


def imoveis():
    os.system('cls')
    while True:
        resposta = menu('IMÓVEIS', 30,['Cadastrar novo imóvel', 'Ver imóveis cadastrados', 'Editar imóvel', 'Apagar imóvel','Menu anterior', 'Sair do sistema'])
        if resposta == 1:  # CADASTRAR IMÓVEIS
            cadastrar_imoveis()
        elif resposta == 2:  # VER IMÓVEIS
            lerimoveis(val)
            sleep(1)
        elif resposta == 3:  # EDITAR IMÓVEIS
            editar_imoveis()
        elif resposta == 4:  # APAGAR IMÓVEIS
            apagar_imoveis()
        elif resposta == 5:
            menuprincipal()
        elif resposta == 6:
            sair()
        else:
            print()
            print(f"{Fore.RED}ERRO! Digite uma opção válida!{Style.RESET_ALL}")

def cadastrar_imoveis():
    os.system('cls')
    ref = None
    print()
    exit_()
    while not ref or len(ref) > 21:
        ref = input('Digite a cidade/estado onde se localiza o imóvel: ').strip()
        if len(ref)>21:
            print()
            print(f"{Fore.RED}Você digitou {len(ref)} caracteres, favor abreviar para no maximo 21.{Style.RESET_ALL}")
            print()
            sleep(0.5)
        elif ref.lower().strip() == 'exit':
            os.system('cls')
            imoveis()
        elif ref == '':
            print("\033[31m""Campo Obrigratório!""\033[0m")
    endereco = ''
    while endereco == '' or verifica_se_existe(endereco, 'imoveis', 'endereço') or len(endereco) > 42:
        endereco = input('Digite o endereço do imóvel (rua, nº, bairro): ').strip()
        if len(endereco) > 42:
            print()
            print(f"{Fore.RED}Você digitou {len(endereco)} caracteres, favor abreviar para no maximo 42.{Style.RESET_ALL}")
            print()
            sleep(0.5)
        elif endereco.lower().strip() == 'exit':
            os.system('cls')
            imoveis()
        elif endereco == '' or verifica_se_existe(endereco, 'imoveis', 'endereço'):
            print(f"{Fore.RED}Endereço inválido ou já existente, digite novamente: {Style.RESET_ALL}")
    cadastrarimoveis(ref, endereco)


def editar_imoveis():
    os.system('cls')
    lerimoveis(val)
    exit_()
    x = input('Digite o número ID do imóvel que deseja editar: ')
    if x.lower().strip() == 'exit':
        os.system('cls')
        imoveis()
    while verifica_ide_existe(x, 'imoveis') or x == '' or x.isalpha():
        print(f"{Fore.RED}ID inválido ou está em um contrato ativo, digite novamente: {Style.RESET_ALL}")
        x = input('Digite o número ID do imóvel que deseja editar: ')
        if x.lower().strip() == 'exit':
            os.system('cls')
            imoveis()
    while True:
        resposta = menu('DIGITE O Nº QUE DESEJA EDITAR', 30,
                        ['Cidade/Estado', 'Endereço', 'Menu anterior', 'Sair do sistema'])
        if resposta == 1:
            ref = None
            while not ref or len(ref) > 21:
                ref = input('Digite a cidade/estado onde se localiza o imóvel: ').strip()
                if len(ref) > 21:
                    print()
                    print(f"{Fore.RED}Você digitou {len(ref)} caracteres, favor abreviar para no máximo 21.{Style.RESET_ALL}")
                    print()
                    sleep(0.5)
                elif ref.lower().strip() == 'exit':
                    os.system('cls')
                    imoveis()
                elif ref == '':
                    print(f"{Fore.RED}Campo Obrigratório!{Style.RESET_ALL}")
            editar(x, 'imoveis', ref, 'ref')
            os.system('cls')
            lerimoveis(x)
        elif resposta == 2:
            endereco = ''
            while endereco == '' or verifica_se_existe(endereco, 'imoveis', 'endereço') or len(endereco) > 42:
                endereco = input('Digite o endereço do imóvel (rua, nº, bairro): ').strip()
                if len(endereco) > 42:
                    print()
                    print(f"{Fore.RED}Você digitou {len(endereco)} caracteres, favor abreviar para no maximo 42.{Style.RESET_ALL}")
                    print()
                    sleep(0.5)
                elif endereco.lower().strip() == 'exit':
                    os.system('cls')
                    imoveis()
                elif endereco == '' or verifica_se_existe(endereco, 'imoveis', 'endereço'):
                    print(f"{Fore.RED}Endereço inválido, digite novamente: {Style.RESET_ALL}")
            editar(x, 'imoveis', endereco, 'endereço')
            lerimoveis(x)
        elif resposta == 3:
            imoveis()
        elif resposta == 4:
            sair()
        else:
            print()
            print(f"{Fore.RED}ERRO! Digite uma opção válida!{Style.RESET_ALL}")

def apagar_imoveis():
    os.system('cls')
    lerimoveis(val)
    exit_()
    x = input('Digite o número id do imóvel que deseja apagar: ')
    if x.lower().strip() == 'exit':
        os.system('cls')
        imoveis()
    while verifica_ide_existe(x, 'imoveis') or x == '' or verifica_se_existe(x, 'contratos','idimoveis') or x.isalpha():
        print(f"{Fore.RED}ID inválido ou está em um contrato ativo, digite novamente: {Style.RESET_ALL}")
        x = input('Digite o número ID do imovel que deseja apagar: ')
        if x.lower().strip() == 'exit':
            os.system('cls')
            imoveis()
    deletar(x, 'imoveis')

def inquilinos():
    os.system('cls')
    while True:
        resposta = menu('INQUILINOS', 35, ['Cadastrar novo inquilino', 'Ver inquilinos cadastrados', 'Editar inquilino',
                                           'Apagar inquilino', 'Menu anterior', 'Sair do sistema'])
        if resposta == 1:  # CADASTRAR INQUILINO
            cadastrar_inquilinos()
        elif resposta == 2:  # VER INQUILINO
            lerinquilinos(val)
            sleep(1)
        elif resposta == 3:  # EDITAR INQUILINO
           editar_inquilino()
        elif resposta == 4:  # APAGAR INQUILINO
            apagar_inquilino()
        elif resposta == 5:
            menuprincipal()
        elif resposta == 6:
            sair()
        else:
            print()
            print(f"{Fore.RED}ERRO! Digite uma opção válida!{Style.RESET_ALL}")

def cadastrar_inquilinos():
    os.system('cls')
    exit_()
    doc = input('Digite o CPF/CNPJ do inquilino: ').strip()
    if doc.lower().strip() == 'exit':
        inquilinos()
    while not validardoc(doc):
        print()
        print(f"{Fore.RED}CPF/CNPJ inválido ou já existente!{Style.RESET_ALL}")
        print()
        doc = input('Digite o CPF/CNPJ do inquilino: ').strip()
        if doc == 'exit':
            os.system('cls')
            inquilinos()
    nome = input('Digite o nome do inquilino: ').strip()
    if nome.lower().strip() == 'exit':
        os.system('cls')
        inquilinos()
    else:
        while nome == '' or verifica_se_existe(nome, 'inquilinos', 'nome') or len(nome) > 31:
            if len(nome) > 31:
                print()
                print(f"{Fore.RED}Você digitou {len(nome)} caracteres, favor abreviar para no maximo 31.{Style.RESET_ALL}")
                print()
                sleep(0.5)
            elif nome == '':
                print(f"{Fore.RED}Nome inválido, digite novamente: {Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Nome já existente. Digite novamente: {Style.RESET_ALL}")
            nome = input('Digite o nome do inquilino: ').strip()
            if nome.lower().strip() == 'exit':
                os.system('cls')
                inquilinos()
    cadastrarinquilinos(nome, doc)

def editar_inquilino():
    os.system('cls')
    lerinquilinos(val)
    exit_()
    x = input('Digite o número ID do inquilino que deseja editar: ')
    if x.lower().strip() == 'exit':
        os.system('cls')
        inquilinos()
    while verifica_ide_existe(x, 'inquilinos') or x == '' or x.isalpha():
        print(f"{Fore.RED}ID inválido ou está em um contrato ativo, digite novamente: {Style.RESET_ALL}")
        x = input('Digite o número ID do inquilino que deseja editar: ')
        if x.lower().strip() == 'exit':
            os.system('cls')
            inquilinos()
    while True:
        resposta = menu('DIGITE O Nº QUE DESEJA EDITAR', 30, ['CPF/CNPJ', 'Nome', 'Menu anterior', 'Sair do sistema'])
        if resposta == 1:
            doc = input('Digite o novo CPF/CNPJ do inquilino: ').strip()
            if doc.lower().strip() == 'exit':
                os.system('cls')
                inquilinos()
            while not validardoc(doc):
                print()
                print(f"{Fore.RED}CPF/CNPJ inválido ou já existente!{Style.RESET_ALL}")
                print()
                doc = input('Digite o novo CPF/CNPJ do inquilino: ').strip()
                if doc.lower().strip() == 'exit':
                    os.system('cls')
                    inquilinos()
            editar(x, 'inquilinos', doc, 'cpf')
            lerinquilinos(x)
        elif resposta == 2:
            nome = input('Digite o novo nome do inquilino: ').strip()
            if nome.lower().strip() == 'exit':
                os.system('cls')
                inquilinos()
            while nome == '' or verifica_se_existe(nome, 'inquilinos', 'nome') or len(nome) > 31:
                if len(nome) > 31:
                    print()
                    print(f"{Fore.RED}Você digitou {len(nome)} caracteres, favor abreviar para no maximo 31.{Style.RESET_ALL}")
                    print()
                    sleep(0.5)
                elif nome == '':
                    print(f"{Fore.RED}Nome inválido, digite novamente: {Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Nome já existente. Digite novamente: {Style.RESET_ALL}")
                nome = input('Digite o nome do inquilino: ').strip()
                if nome.lower().strip() == 'exit':
                    os.system('cls')
                    inquilinos()
            editar(x, 'inquilinos', nome, 'nome')
            lerinquilinos(x)
        elif resposta == 3:
            inquilinos()
        elif resposta == 4:
            sair()
        else:
            print()
            print(f"{Fore.RED}ERRO! Digite uma opção válida!{Style.RESET_ALL}")

def apagar_inquilino():
    os.system('cls')
    lerinquilinos(val)
    exit_()
    x = input('Digite o número ID do inquilino que deseja apagar: ')
    if x.lower().strip() == 'exit':
        os.system('cls')
        inquilinos()
    while verifica_ide_existe(x, 'inquilinos') or x == '' or verifica_se_existe(x, 'contratos','idinquilinos') or x.isalpha():
        print(f"{Fore.RED}ID inválido ou está em um contrato ativo, digite novamente: {Style.RESET_ALL}")
        x = input('Digite o número ID do inquilino que deseja apagar: ')
        if x.lower().strip() == 'exit':
            os.system('cls')
            inquilinos()
    deletar(x, 'inquilinos')
def sair():
    os.system('cls')
    cabeçalho('Saindo do sistema... Até Logo!', 32)
    sleep(1)
    os._exit(0)

exibir_tela_inicial()
menuprincipal()