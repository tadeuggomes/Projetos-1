import json
import os
from time import sleep

class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'


arquivo_fornecedores = os.path.join(os.path.dirname(__file__), 'fornecedores.json')

def carregar_fornecedores():
    if not os.path.exists(arquivo_fornecedores):
        with open(arquivo_fornecedores, 'w') as f:
            json.dump([], f, indent=4)
    with open(arquivo_fornecedores, 'r') as f:
        return json.load(f)

def adicionar_fornecedor(cnpj):
    fornecedores = carregar_fornecedores()
    fornecedores.append({'cnpj': cnpj})
    with open(arquivo_fornecedores, 'w') as f:
        json.dump(fornecedores, f, indent=4, ensure_ascii=False)
    print("FORNECEDOR ADICIONADO COM SUCESSO!")

def listar_fornecedores():
    fornecedores = carregar_fornecedores()
    if fornecedores:
        print("=" * 50)
        print("LISTA DE FORNECEDORES:")
        print("-" * 50)
        for fornecedor in fornecedores:
            print(f"CNPJ: {fornecedor['cnpj']}")
            print("*" * 50)
        print("=" * 50)
    else:
        print("NENHUM FORNECEDOR CADASTRADO.")

def atualizar_fornecedor(antigo_cnpj, novo_cnpj):
    fornecedores = carregar_fornecedores()
    for fornecedor in fornecedores:
        
        if fornecedor['cnpj'] == antigo_cnpj:
            fornecedor['cnpj'] = novo_cnpj
            print("FORNECEDOR ATUALIZADO COM SUCESSO!")
            break
    else:
        print("FORNECEDOR NÃO ENCONTRADO.")
    
    with open(arquivo_fornecedores, 'w') as f:
        json.dump(fornecedores, f, indent=4, ensure_ascii=False)

def excluir_fornecedor(cnpj):
    fornecedores = carregar_fornecedores()
    encontrado_2 = False
    for fornecedor in fornecedores:
        if fornecedor['cnpj'] == cnpj:
            fornecedores.remove(fornecedor)  
            encontrado_2 = True
            print(f"CNPJ: {fornecedor['cnpj']} EXCLUÍDO COM SUCESSO!")
            break 

    with open(arquivo_fornecedores, 'w') as f:
        json.dump(fornecedores, f, indent=4, ensure_ascii=False)

    if not encontrado_2:
        print("NENHUM FORNECEDOR ENCONTRADO COM ESSE CNPJ.")
        
def buscar_fornecedor(cnpj):
    fornecedores = carregar_fornecedores()
    encontrado = False
    for fornecedor in fornecedores:
        if fornecedor['cnpj'] == cnpj:
            print(f"CNPJ: {fornecedor['cnpj']}, CNPJ: {fornecedor['cnpj']}")
            encontrado = True
    if not encontrado:
        print("NENHUM FORNECEDOR CADASTRADO.")

def menu_fornecedor():
    print(cor.CIANO + "=" * 55 + cor.RESET)
    print(cor.VERMELHO + " ---->>> BEM VINDO AO SISTEMA DE FORNECEDORES <<<---- ")
    print("1 - ADICIONAR FORNECEDOR")
    print("2 - LISTAR FORNECEDORES")
    print("3 - ATUALIZAR FORNECEDOR")
    print("4 - EXCLUIR FORNECEDOR")
    print("5 - BUSCAR FORNECEDOR")
    print("6 - SAIR")
    print(cor.CIANO + "=" * 55 + cor.RESET)

def main():
    while True:
        menu_fornecedor()
        opcao = input("ESCOLHA UMA OPÇÃO:\n>>> ")

        match opcao:
            case "1":
                cnpj = input("DIGITE O CNPJ DO FORNECEDOR:\n>>> ")
                adicionar_fornecedor(cnpj)
            case "2":
                listar_fornecedores()
            case "3":
                antigo_cnpj = input("DIGITE O CNPJ A SER ATUALIZADO:\n>>> ")
                novo_cnpj = input("DIGITE O NOVO CNPJ:\n>>> ")
                atualizar_fornecedor(antigo_cnpj,novo_cnpj)
            case "4":
                cnpj = input("DIGITE O CNPJ DO FORNECEDOR A SER EXCLUÍDO:\n>>> ")
                excluir_fornecedor(cnpj)
            case "5":
                cnpj = input("DIGITE O CNPJ DO FORNECEDOR:\n>>> ")
                buscar_fornecedor(cnpj)
            case "6":
                print("FECHANDO PROGRAMA...")
                sleep(3)
                break
            case _:
                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()