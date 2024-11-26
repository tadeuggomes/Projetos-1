import json
import os 
from time import sleep 


arquivo = os.path.join(os.path.dirname(__file__), 'cliente.json')

def carregar_cliente():
    if not os.path.exists(arquivo):
        
        with open(arquivo, 'w') as f:
            
            json.dump({}, f, indent=4)
            
    with open(arquivo, 'r') as f:
        return json.load(f)
        
    

    
def add_clientes(cpf, idade, cep):
    clientes=carregar_cliente()
    
    clientes.append({'cpf': cpf, 'idade': idade, 'CEP': cep})
    with open(arquivo, 'w') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)
    print('👤 CLIENTE ADICIONADO!!!')
    
def atualizar_cadastro_clientes(cpf_velho, cpf_novo, idade_nova, cep_novo):
    clientes = carregar_cliente()
    cliente_encontrado = False
    
    for cliente in clientes:
        if cliente['cpf'] == cpf_velho:
            cliente['cpf'] = cpf_novo
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
            print(f"CPF: {cliente['cpf']}")
            print(f"Idade: {cliente['idade']}")
            print(f"CEP: {cliente['CEP']}")
            print("-" * 60)
    else:
        print("❌ NÃO TEM CLIENTES CADASTRADOS!!!")
        
def excluir_clientes(cpf): 
    clientes = carregar_cliente()
    cliente_encontrado = False 
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            clientes.remove(cliente) 
            cliente_encontrado = True  
            break
    if cliente_encontrado:
        with open(arquivo, 'w') as f:
            json.dump(clientes, f, indent=4, ensure_ascii=False)
        print("✅ CLIENTE EXCLUÍDO COM SUCESSO!!!")
    else:
        print("❌ ERRO: CLIENTE NÃO ENCONTRADO NO SISTEMA!!!")
        
def buscar_cliente(cpf):
    
    clientes = carregar_cliente()
    encontrado = False

    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print(f"CPF: {cliente['cpf']}, IDADE: {cliente['idade']}, CEP: {cliente['CEP']}")
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
                        cpf = input(" INFORME O CPF:\n>>>")
                        idade = input(" INFORME A IDADE:\n>>>")
                        cep = input(" INFORME O CEP:\n>>>")
                        add_clientes(cpf, idade, cep)
                    elif opcao_cliente == "2":
                        listar_clientes()
                    elif opcao_cliente == "3":
                        cpf_velho = input("DIGITE O CPF A SER ATUALIZADO:\n>>>")
                        cpf_novo = input("DIGITE O NOVO CPF:\n>>>")
                        idade_nova = input("DIGITE A NOVA IDADE:\n>>>")
                        cep_novo = input("DIGITE O NOVO CEP:\n>>>")
                        atualizar_cadastro_clientes(cpf_velho, cpf_novo , idade_nova, cep_novo)
                    elif opcao_cliente == "4":
                        cpf = input("INSIRA O CPF DO USUÁRIO A SER EXCLUÍDO:\n>>>")
                        excluir_clientes(cpf)
                    elif opcao_cliente == "5":
                        cpf = input("INSIRA O CPF DO USUÁRIO:\n>>>")
                        buscar_cliente(cpf)
                    elif opcao_cliente == "6":
                        print("VOLTANDO AO MENU ANTERIOR...")
                        sleep(1)
                        break
                    else:
                        print("❌ OPÇÃO NÃO EXISTENTE. INSIRA OUTRA OPÇÃO!!!")
            case 2:
                print("🚀 SAINDO....")
                sleep(1)
                break
            case __:
                print("❌ OPÇÃO NÃO EXISTENTE. INSIRA OUTRA OPÇÃO!!!")

if __name__ == "__main__":
    main()
