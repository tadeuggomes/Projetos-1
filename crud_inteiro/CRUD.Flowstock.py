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

#Caminho do Arquivo JSON
arquivo_cliente = os.path.join(os.path.dirname(__file__), 'cliente.json')
arquivo_produto = os.path.join(os.path.dirname(__file__), 'produtos.json')
arquivo_fornecedores = os.path.join(os.path.dirname(__file__), 'fornecedores.json') 

def carregar_cliente():
    if not os.path.exists(arquivo_cliente):
        with open(arquivo_cliente, 'w') as f:
            json.dump([], f, indent=4)
    with open(arquivo_cliente, 'r') as f:
        return json.load(f) 

def carregar_produto():
    if not os.path.exists(arquivo_produto):
        with open(arquivo_produto, 'w') as f:
            json.dump([], f, indent=4)
    with open(arquivo_produto, 'r') as f:
        return json.load(f) 

def carregar_fornecedores():
    if not os.path.exists(arquivo_fornecedores):
        with open(arquivo_fornecedores, 'w') as f:
            json.dump([], f, indent=4)
    with open(arquivo_fornecedores, 'r') as f:
        return json.load(f)

# CRUD DO CLIENTE 

def adicionar_clientes(nome, idade, cep):
    clientes = carregar_cliente()
    
    # Adiciona o novo cliente à lista
    clientes.append({'nome': nome, 'idade': idade, 'CEP': cep})
    
    # Abre o arquivo no modo de escrita
    with open(arquivo_cliente, 'w') as f:
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
        with open(arquivo_cliente, 'w') as f:
            json.dump(clientes, f, indent=4, ensure_ascii=False)
        print("✅ CLIENTE ATUALIZADO!!!")
    else:
        print("❌ ERRO: CLIENTE NÃO EXISTE NO SISTEMA!!!")

def listar_clientes():
    clientes = carregar_cliente()
    
    if clientes:
        print("👤 LISTA DE CLIENTES:")
        for cliente in clientes:
            print(f"Nome: {cliente['nome']}")
            print(f"Idade: {cliente['idade']}")
            print(f"CEP: {cliente['CEP']}")
    else:
        print("❌ NÃO TEM CLIENTES CADASTRADOS!!!") 

def excluir_clientes(nome):
    clientes = carregar_cliente()
    cliente_encontrado = False 
    for cliente in clientes:
        if cliente['nome'] == nome:
            clientes.remove(cliente) 
            cliente_encontrado = True  
            break
    if cliente_encontrado:
        with open(arquivo_cliente, 'w') as f:
            json.dump(clientes, f, indent=4, ensure_ascii=False)
        print("✅ CLIENTE EXCLUÍDO COM SUCESSO!!!")
    else:
        print("❌ ERRO: CLIENTE NÃO ENCONTRADO NO SISTEMA!!!") 

def buscar_cliente(nome):
    clientes = carregar_cliente()
    encontrado = False

    for cliente in clientes:
        if cliente['nome'] == nome:
            print(f"NOME: {cliente['nome']}, IDADE: {cliente['idade']}, CEP: {cliente['CEP']}")
            encontrado = True
    if not encontrado:
        print("❌ CLIENTE NÃO CADASTRADO!!!")

# CRUD DO PRODUTO 

def adicionar_produto(produto, preco, codigo):
    produtos = carregar_produto()
    produtos.append({'bebida': produto,'preco': preco, 'codigo': codigo})
    
    with open(arquivo_produto, 'w') as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)
    print("🍺 PRODUTO ADICIONADO COM SUCESSO!") 

def listar_produto(): 
    produtos = carregar_produto()
    if  produtos:  
        print("LISTA DE PRODUTOS:")
        for produto in produtos:
            print(f"PRODUTO: {produto.get('bebida')}")
            print(f"PREÇO: {produto.get('preco')}")
            print(f"CÓDIGO: {produto.get('codigo')}")
    
    else:
        print("Obs: A Lista está vazia!") 

def atualizar_produto(produto_antigo, produto_novo, preco_novo, codigo_novo):
    produtos = carregar_produto()
    produto_encontrado = False
    for produto in produtos:
        if produto.get('bebida') == produto_antigo:
            produto['bebida'] = produto_novo
            produto['preco'] = preco_novo
            produto['codigo'] = codigo_novo
            produto_encontrado = True
            break

    if produto_encontrado:
        with open(arquivo_produto, 'w') as f:
            json.dump(produtos, f, indent=4, ensure_ascii=False) 
        print("✅ PRODUTO ATUALIZADO COM SUCESSO!")
    else:
        print("⚠️ PRODUTO NÃO ENCONTRADO PARA ATUALIZAÇÃO.") 

def excluir_produto(nome_produto):
    produtos = carregar_produto()           
                                             
    for produto in produtos:                 
        if produto.get('bebida') == nome_produto:
            produtos.remove(produto)        

    print(f"Produto '{nome_produto}")

    with open(arquivo_produto, 'w') as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)
    print("❌ PRODUTO EXCLUÍDO COM SUCESSO!")

# CRUD DOS FORNCEDORES 

def adicionar_fornecedor(cnpj):
    fornecedores = carregar_fornecedores()
    fornecedores.append({'cnpj': cnpj})
    with open(arquivo_fornecedores, 'w') as f:
        json.dump(fornecedores, f, indent=4, ensure_ascii=False)
    print("FORNECEDOR ADICIONADO COM SUCESSO!") 

def listar_fornecedores():
    fornecedores = carregar_fornecedores()
    if fornecedores:
        print("LISTA DE FORNECEDORES:")
        for fornecedor in fornecedores:
            print(f"CNPJ: {fornecedor['cnpj']}")
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

#MENUS 
def menu_inicial():
    print("---->>> FLOWSTOCK <<<---- ")
    print(" 1 - MENU CLIENTE ")
    print(" 2-  MENU DO PRODUTO") 
    print(" 3 - MENU DO FORNECEDOR")
    print(" 4 - SAIR ") 
    
def exibir_menu_cliente():
    
    print("---->>> MENU CLIENTE <<<---- ")
    print(" 1. ADICIONAR CLIENTE")
    print(" 2. LISTAR CLIENTES")
    print(" 3. ATUALIZAR CADASTRO DO CLIENTE")
    print(" 4. EXCLUIR CLIENTE")
    print(" 5. LISTAR UM CLIENTE")
    print(" 6. VOLTAR AO MENU ANTERIOR") 
    

def exibir_menu_produto():
    
    print("\n ---->>> MENU PRODUTO <<<----:")
    print("1. ADICIONAR PRODUTO")
    print("2. LISTAR PRODUTO")
    print("3. ATUALIZAR PRODUTO")
    print("4. EXCLUIR PRODUTO")
    print("5. VOLTAR AO MENU ANTERIOR")
    

def exibir_menu_fornecedor():
    
    print(" ---->>> MENU DO FORNECEDOR <<<---- ")
    print("1 - ADICIONAR FORNECEDOR")
    print("2 - LISTAR FORNECEDORES")
    print("3 - ATUALIZAR FORNECEDOR")
    print("4 - EXCLUIR FORNECEDOR")
    print("5 - BUSCAR FORNECEDOR")
    print("6 - SAIR")

def main():
    
    while True:
        menu_inicial()
        opcao_inicio = int(input("INFORME UMA OPÇÃO:\n>>>"))

        match (opcao_inicio):
            case 1:
                while True: 
                    exibir_menu_cliente()
                    opcao_cliente = input("ESCOLHA UMA OPÇÃO:\n>>>")

                    if opcao_cliente == "1":
                        nome = input(" INFORME O NOME:\n>>>")
                        idade = input(" INFORME A IDADE:\n>>>")
                        cep = input(" INFORME O CEP:\n>>>")
                        adicionar_clientes(nome, idade, cep)
                        
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
                while True:
                    exibir_menu_produto()
                    opcao_produto = input("ESCOLHA UMA OPÇÃO:\n>>>")

                    if opcao_produto == "1":
                        produto = input("INFORME UMA BEBIDA:\n>>>")
                        preco = float(input("DIGITE O PREÇO:\n>>>"))
                        codigo = input("INFORME O CODIGO DO PRODUTO:\n>>>")
                        adicionar_produto(produto, preco, codigo)
                        
                    elif opcao_produto == "2":
                        listar_produto()
                        
                    elif opcao_produto == "3":
                        produto_antigo = input("INFORME UMA BEBIDA PARA SER ATUALIZADA:\n>>>")
                        produto_novo = input("INFORME UMA NOVA BEBIDA:\n>>>")
                        preco_novo = float(input("DIGITE O NOVO PREÇO:\n>>>"))
                        codigo_novo = input("INFORME O NOVO CÓDIGO DO PRODUTO:\n>>>")
                        atualizar_produto(produto_antigo, produto_novo, preco_novo, codigo_novo)
                        
                    elif opcao_produto == "4":
                        produto = input("DIGITE O NOME DA BEBIDA A SER EXCLUÍDA:\n>>>")
                        excluir_produto(produto)
                        
                    elif opcao_produto == "5":
                        print("VOLTAR AO MENU ANTERIOR...")
                        sleep(3)
                        break
                    else:
                        print("⚠️ OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 3: 
                while True:
                    exibir_menu_fornecedor()
                    opcao_fornecedor = input("ESCOLHA UMA OPÇÃO:\n>>> ")

                    match opcao_fornecedor:
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
            case 4: 
                print("🚀 SAINDO...")
                sleep(3)
                break 
            
            case _:
                print("⚠️ OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()
