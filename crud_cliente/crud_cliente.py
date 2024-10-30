import json #Manipular dados em JSON
import os #Fazer operações de sistema, como verificar e manipular arquivos
from time import sleep #Criar pausas controladas durante a execução

# Definindo o caminho do arquivo no escopo global:
arquivo = os.path.join(os.path.dirname(__file__), 'cliente.json')

def carregar_cliente():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)
    with open(arquivo, 'r') as f:
        return json.load(f) 
def add_cliente(nome, idade, cep):
    cliente=carregar_cliente()
    
    cliente.append({'nome': nome, 'idade': idade, 'CEP': cep})
    with open(arquivo, 'w') as f:
        json.dump(cliente, f)
    print('CLIENTE ADICIONADO!!')
    nome = input(" DIGITE O NOME:\n>>>")
    idade = input(" DIGITE A IDADE:\n>>>")
    cep= input("DIGITE O CEP:\n>>>")
    add_cliente(nome, idade,cep)
    
#0. CARREGAR CLIENTE- TADEU
#1. ADICIONAR CLIENTE- TADEU
#2. LISTAR UCLIENTES- TADEU
#3. ATUALIZAR CLIENTE- TADEU
#4. EXCLUIR CLIENTE- DAVID
#5. LISTAR UM CLIENTE DAVID
#6. VOLTAR AO MENU ANTERIOR- DAVID
#7. ENCERRAR CADASTRO