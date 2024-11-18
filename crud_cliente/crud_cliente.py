import json #Manipular dados em JSON
import os #Fazer operações de sistema, como verificar e manipular arquivos
from time import sleep #Criar pausas controladas durante a execução

# Definindo o caminho do arquivo no escopo global:
arquivo = os.path.join(os.path.dirname(__file__), 'cliente.json')

# w - escrever
# R - ler
def carregar_cliente():
    if not os.path.exists(arquivo):
        # Verifica se o arquivo (armazenado na variável 'arquivo') existe. 'os.path.exists' retorna False se o arquivo não existir
        with open(arquivo, 'w') as f:
            # O modo 'w' cria um arquivo vazio ou substitui um arquivo existente.
            json.dump({}, f, indent=4)
            # Salva uma lista vazia no arquivo JSON recém-criado, formatado com indentação para legibilidade. Isso cria uma estrutura de dados JSON válida para evitar erros ao tentar ler o arquivo depois.
    with open(arquivo, 'r') as f:
        return json.load(f)
        # Carrega e retorna os dados JSON do arquivo como uma lista ou dicionário. Caso o arquivo esteja vazio, ele retornará uma lista vazia (inicializada na etapa anterior).
    
def add_clientes(nome, idade, cep):
    clientes=carregar_cliente()
    
    clientes.append({'nome': nome, 'idade': idade, 'CEP': cep})
    with open(arquivo, 'w') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)
    print('👤 CLIENTE ADICIONADO!!!')
    
def atualizar_cadastro_clientes(nome_velho, nome_novo, idade_nova, cep_novo):
    clientes = carregar_cliente()
    cliente_encontrado = False
    
    for cliente in clientes:
        if cliente['nome'] == nome_velho:
            cliente['nome'] = nome_novo
            cliente['idade'] = idade_nova
            cliente['CEP'] = cep_novo
            cliente_encontrado = True
            break

    if cliente_encontrado:
        with open(arquivo, 'w') as f:
            json.dump(clientes, f, indent=4, ensure_ascii=False)
        print("✅ CLIENTE ATUALIZADO!!!")
    else:
        print("❌ ERRO: CLIENTE NÃO EXISTE NO SISTEMA!!!")
   
def listar_clientes():
    clientes = carregar_cliente()
    
    if clientes:
        print("-" * 60)
        print("👤 LISTA DE CLIENTES:")
        for cliente in clientes:
            print("-" * 60)
            print(f"Nome: {cliente['nome']}")
            print(f"Idade: {cliente['idade']}")
            print(f"CEP: {cliente['CEP']}")
            print("-" * 60)
    else:
        print("❌ NÃO TEM CLIENTES CADASTRADOS!!!")
        
def excluir_clientes(nome): #Se o cliente existir no sistema, ele será excluído. Caso contrário, uma mensagem informando que o cliente não foi encontrado será exibida.
    clientes = carregar_cliente()
    cliente_encontrado = False 
    for cliente in clientes:
        if cliente['nome'] == nome:
            clientes.remove(cliente) 
            cliente_encontrado = True  
            break
    if cliente_encontrado:
        with open(arquivo, 'w') as f:
            json.dump(clientes, f, indent=4, ensure_ascii=False)
        print("✅ CLIENTE EXCLUÍDO COM SUCESSO!!!")
    else:
        print("❌ ERRO: CLIENTE NÃO ENCONTRADO NO SISTEMA!!!")
        
def buscar_cliente(nome):
    #Busca e exibe os dados de um cliente especifico, pelo nome.
    #Se o cliente não for encontrado, informa que o cliente não foi cadastrado
    clientes = carregar_cliente()
    encontrado = False

    for cliente in clientes:
        if cliente['nome'] == nome:
            print(f"NOME: {cliente['nome']}, IDADE: {cliente['idade']}, CEP: {cliente['CEP']}")
            encontrado = True
    if not encontrado:
        print("❌ CLIENTE NÃO CADASTRADO!!!")
    
def menu_inicial():
  
    print(" ---->>> FLOWSTOCK <<<---- ")
    print(" 1 - MENU CLIENTE ")
    print(" 2 - SAIR ")
    
def exibir_menu():
    print(" ---->>> MENU CLIENTE <<<---- ")
    print(" 1. ADICIONAR CLIENTE")
    print(" 2. LISTAR CLIENTES")
    print(" 3. ATUALIZAR CADASTRO DO CLIENTE")
    print(" 4. EXCLUIR CLIENTE")
    print(" 5. LISTAR UM CLIENTE")
    print(" 6. VOLTAR AO MENU ANTERIOR")

def main():
    
    while True:
        menu_inicial()
        opcao_inicio = int(input("INFORME UMA OPÇÃO:\n>>>"))

        match (opcao_inicio):
            case 1:
                while True: 
                    exibir_menu()
                    opcao_cliente = input("ESCOLHA UMA OPÇÃO:\n>>>")

                    if opcao_cliente == "1":
                        nome = input(" INFORME O NOME:\n>>>")
                        idade = input(" INFORME A IDADE:\n>>>")
                        cep = input(" INFORME O CEP:\n>>>")
                        add_clientes(nome, idade, cep)
                    elif opcao_cliente == "2":
                        listar_clientes()
                    elif opcao_cliente == "3":
                        nome_velho = input("DIGITE O NOME A SER ATUALIZADO:\n>>>")
                        nome_novo = input("DIGITE O NOVO NOME:\n>>>")
                        idade_nova = input("DIGITE A NOVA IDADE:\n>>>")
                        cep_novo = input("DIGITE O NOVO CEP:\n>>>")
                        atualizar_cadastro_clientes(nome_velho, nome_novo , idade_nova, cep_novo)
                    elif opcao_cliente == "4":
                        nome = input("INSIRA O NOME DO USUÁRIO A SER EXCLUÍDO:\n>>>")
                        excluir_clientes(nome)
                    elif opcao_cliente == "5":
                        nome = input("INSIRA O NOME DO USUÁRIO:\n>>>")
                        buscar_cliente(nome)
                    elif opcao_cliente == "6":
                        print("VOLTANDO AO MENU ANTERIOR...")
                        sleep(1)
                        break
                    else:
                        print("❌ OPÇÃO NÃO EXISTENTE. INSIRA OUTRA OPÇÃO!!!")
            case 2:
                print("🚀 SAINDO...")
                sleep(1)
                break
            case __:
                print("❌ OPÇÃO NÃO EXISTENTE. INSIRA OUTRA OPÇÃO!!!")

if __name__ == "__main__":
    main()