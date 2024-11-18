import json #Manipular dados em JSON
import os #Fazer operações de sistema, como verificar e manipular arquivos
from time import sleep #Criar pausas controladas durante a execução do programa

# Definindo o caminho do arquivo no escopo global:
arquivo = os.path.join(os.path.dirname(__file__), 'produtos.json') 

def carregar_produto():
    # Verifica se o arquivo (armazenado na variável 'arquivo') existe. 'os.path.exists' retorna False se o arquivo não existir
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)  # Inicializa como lista vazia 
              # json.dump -> serve para gravar (salvar) um objeto em arquivo json
              # Salva uma lista vazia no arquivo JSON recém-criado, formatado com indentação para legibilidade. 
              # Isso cria uma estrutura de dados JSON válida para evitar erros ao tentar ler o arquivo depois.
    with open(arquivo, 'r') as f: # r -> read 
        return json.load(f)

def adicionar_produto(produto, preco, codigo):
    produtos = carregar_produto()
    produtos.append({'bebida': produto,'preco': preco, 'codigo': codigo})
    
    with open(arquivo, 'w') as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)
    print("🍺 PRODUTO ADICIONADO COM SUCESSO!")


def listar_produto(): 
    produtos = carregar_produto()
    if  produtos:  
        print("LISTA DE PRODUTOS:")
        for produto in produtos:
            print(f"PRODUTO: {produto.get('bebida')}") #O método .get() permite que você busque o valor associado
                                                       #a uma chave específica em um dicionário.
            print(f"PREÇO: {produto.get('preco')}")
            print(f"CÓDIGO: {produto.get('codigo')}")
    
    else:
        print("Obs: A Lista está vazia!")

def atualizar_produto(produto_antigo, produto_novo, preco_novo, codigo_novo):
    produtos = carregar_produto()
    produto_encontrado = False
    for produto in produtos:
        if produto.get('bebida') == produto_antigo: #get -> retorna a lista
            produto['bebida'] = produto_novo
            produto['preco'] = preco_novo
            produto['codigo'] = codigo_novo
            produto_encontrado = True
            break

    if produto_encontrado:
        with open(arquivo, 'w') as f: # abrir arquivo no modo escrita
            json.dump(produtos, f, indent=4, ensure_ascii=False) #GRAVAR O ARQUIVO DENTRO DO CÓDIGO JSON
        print("✅ PRODUTO ATUALIZADO COM SUCESSO!")
    else:
        print("⚠️ PRODUTO NÃO ENCONTRADO PARA ATUALIZAÇÃO.")

def excluir_produto(nome_produto):
    produtos = carregar_produto()            # Carrega a lista de produtos
                                             # Encontra e remove o produto da lista usando a função remove()
    for produto in produtos:                 # Usa uma cópia da lista para evitar problemas durante a iteração
        if produto.get('bebida') == nome_produto:
            produtos.remove(produto)         # Remove o produto se o nome corresponder

    print(f"Produto '{nome_produto}")

    with open(arquivo, 'w') as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)
    print("❌ PRODUTO EXCLUÍDO COM SUCESSO!")

def menu_inicial():
    print(" ----FLOWSTOCK---- ")
    print(" 1 - MÓDULO ESTOQUE ")
    print(" 2 - SAIR ") 

def exibir_menu_produto():
    print("\nMENU:")
    print("1. ADICIONAR PRODUTO")
    print("2. LISTAR PRODUTO")
    print("3. ATUALIZAR PRODUTO")
    print("4. EXCLUIR PRODUTO")
    print("5. VOLTAR AO MENU ANTERIOR")

def main():
    while True:
        menu_inicial()
        opcao_inicial = int(input("INFORME UMA OPÇÃO: "))

        match opcao_inicial:
            case 1:
                while True:
                    exibir_menu_produto()
                    opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")

                    if opcao == "1":
                        produto = input("INFORME UMA BEBIDA:\n>>>")
                        preco = float(input("DIGITE O PREÇO:\n>>>"))
                        codigo = input("INFORME O CODIGO DO PRODUTO:\n>>>")
                        adicionar_produto(produto, preco, codigo)
                    elif opcao == "2":
                        listar_produto()
                    elif opcao == "3":
                        produto_antigo = input("INFORME UMA BEBIDA PARA SER ATUALIZADA:\n>>>")
                        produto_novo = input("INFORME UMA NOVA BEBIDA:\n>>>")
                        preco_novo = float(input("DIGITE O NOVO PREÇO:\n>>>"))
                        codigo_novo = input("INFORME O NOVO CÓDIGO DO PRODUTO:\n>>>")
                        atualizar_produto(produto_antigo, produto_novo, preco_novo, codigo_novo)
                    elif opcao == "4":
                        produto = input("DIGITE O NOME DA BEBIDA A SER EXCLUÍDA:\n>>>")
                        excluir_produto(produto)
                    elif opcao == "5":
                        print("VOLTAR AO MENU ANTERIOR...")
                        sleep(3)
                        break
                    else:
                        print("⚠️ OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 2:
                print("🚀 SAINDO...")
                sleep(3)
                break
            case _:
                print("⚠️ OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()
