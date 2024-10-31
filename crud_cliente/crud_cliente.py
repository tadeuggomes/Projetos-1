import json #Manipular dados em JSON
import os #Fazer operações de sistema, como verificar e manipular arquivos
from time import sleep #Criar pausas controladas durante a execução

# Definindo o caminho do arquivo no escopo global:
arquivo = os.path.join(os.path.dirname(__file__), 'cliente.json')

def carregar_cliente():
    # Define a função 'carregar_cliente' para carregar os dados dos clientes a partir de um arquivo JSON.
    if not os.path.exists(arquivo):
        # Verifica se o arquivo (armazenado na variável 'arquivo') existe.
        # 'os.path.exists' retorna False se o arquivo não existir
        with open(arquivo, 'w') as f:
            # Se o arquivo não existe, ele é criado no modo de escrita ('w').
            # O modo 'w' cria um arquivo vazio ou substitui um arquivo existente.
            json.dump([], f, indent=4)
            # Salva uma lista vazia no arquivo JSON recém-criado, formatado com indentação para legibilidade.
            # Isso cria uma estrutura de dados JSON válida para evitar erros ao tentar ler o arquivo depois.
    with open(arquivo, 'r') as f:
        # Abre o arquivo no modo de leitura ('r').
        return json.load(f)
        # Carrega e retorna os dados JSON do arquivo como uma lista ou dicionário.
        # Caso o arquivo esteja vazio, ele retornará uma lista vazia (inicializada na etapa anterior).
    
def add_clientes(nome, idade, cep):
    clientes=carregar_cliente()
    
    clientes.append({'nome': nome, 'idade': idade, 'CEP': cep})
    with open(arquivo, 'w') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)
    print('CLIENTE ADICIONADO!!')
    
def atualizar_cadastro_clientes(nome_velho, nome_novo , idade_nova, cep_novo):
    clientes= carregar_cliente()

    for cliente in clientes:
        if cliente['nome'] == nome_velho:
            cliente['nome']= nome_novo
            cliente['idade'] = idade_nova
            cliente['CEP'] = cep_novo            
            break
    with open(arquivo, 'w') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)
    print("CLIENTE ATUALIZADO!!!") 
   
    nome_velho = input("DIGITE O NOME A SER ATUALIZADO:\n>>>")
    nome_novo = input("DIGITE O NOVO NOME:\n>>>")
    idade_nova = input("DIGITE A NOVA IDADE:\n>>>")
    cep_novo = input("DIGITE O NOVO CEP:\n>>>")
    atualizar_cadastro_clientes(nome_velho, nome_novo , idade_nova, cep_novo)

def listar_clientes():
    clientes = carregar_cliente()
    
    if clientes:
        print("-" * 60)
        print("LISTA DE CLIENTES:")
        for cliente in clientes:
            print("-" * 60)
            print(f"Nome: {cliente['nome']}")
            print(f"Idade: {cliente['idade']}")
            print(f"CEP: {cliente['CEP']}")
            print("-" * 60)
    else:
        print("NÃO TEM CLIENTES CADASTRADOS.")
        






















#0. CARREGAR CLIENTE- TADEU 
#1. ADICIONAR CLIENTE- TADEU
#2. LISTAR CLIENTES- TADEU
#3. ATUALIZAR CLIENTE- TADEU

#4. EXCLUIR CLIENTE- DAVID
#5. LISTAR UM CLIENTE DAVID
#6. VOLTAR AO MENU ANTERIOR- DAVID

#7. ENCERRAR CADASTRO