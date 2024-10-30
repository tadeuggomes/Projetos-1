import json #Manipular dados em JSON
import os #Fazer operações de sistema, como verificar e manipular arquivos
from time import sleep #Criar pausas controladas durante a execução

# Definindo o caminho do arquivo no escopo global:
arquivo = os.path.join(os.path.dirname(__file__), 'cliente.json')

# essa funçao ela vai carregar os clientes já existentes e se não tiver um cliente ela abre um novo espaço para por exemplo, add um cliente novo.
def carregar_cliente():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)
    with open(arquivo, 'r') as f:
        return json.load(f) 
def add_clientes(nome, idade, cep):
    clientes=carregar_cliente()
    
    clientes.append({'nome': nome, 'idade': idade, 'CEP': cep})
    with open(arquivo, 'w') as f:
        json.dump(clientes, f)
    print('CLIENTE ADICIONADO!!')
    

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
        
listar_clientes()








#0. CARREGAR CLIENTE- TADEU 
#1. ADICIONAR CLIENTE- TADEU
#2. LISTAR CLIENTES- TADEU
#3. ATUALIZAR CLIENTE- TADEU

#4. EXCLUIR CLIENTE- DAVID
#5. LISTAR UM CLIENTE DAVID
#6. VOLTAR AO MENU ANTERIOR- DAVID

#7. ENCERRAR CADASTRO