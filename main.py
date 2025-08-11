from funcionario import Funcionario

def cadastrar_funcionario():
    nome =  input("Digite o nome do funcionário: ")
    idade = int(input("Digite a idade do funcionário: "))
    cpf = input("Digite o CPF do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    contrato = input("Digite o tipo de contrato do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    novo_funcionario = Funcionario(nome, idade, cpf, cargo, contrato, setor)
    funcionarios.append(novo_funcionario)
    print("Funcionário cadastrado com sucesso!")

def listar_funcionario():
    for func in funcionarios:
        print(func)
        print("\n")
        print("Fim da lista de Funcionários")

def buscar_funcionario():
    cpf = input("Digite o cpf do funcionario que deseja buscar:")
    for func in funcionarios:
        if func.cpf == cpf:
            return func
        
        else: 
            print("Funcionário não encontrado!")
            return None

def excluir_funcionario():
    cpf = input("Digite o CPF do funcionário que deseja excluir: ")
    for func in funcionarios:
        if func.cpf == cpf:
            funcionarios.remove(func)
            return f'Funcionário removido com sucesso!'
        
        else:
            print("Funcionário não encontrado!")
            return None

opcao = 0
menu = True
funcionarios = []
while menu:
    print(f'''
MENU:
          1 - Cadastrar Funcionário
          2 - Listar Funcionários
          3 - Buscar Funcionário
          4 - Excluir Funcionário
          5 - Sair
''')
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_funcionario()

    elif opcao == 2:
        listar_funcionario()
    
    elif opcao == 3:
        buscar_funcionario()
    
    elif opcao == 4:
        excluir_funcionario()

    elif opcao == 5:
        print("Saindo do sistema...")

    else:
        print("Opção inválida. Tente novamente!")
        continue