from funcionario import Funcionario

def cadastrar_funcionario():
    nome =  input("Digite o nome do funcionário: ")

    while True:
        try:
            idade = int(input("Digite a idade do funcionário: "))
            if 18 <= idade <= 80:
                break
            print("Idade inválida! Deve estar entre 18 e 100 anos.")
        except ValueError:
            print("Idade inválida! Digite apenas números inteiros.")

    while True:
        cpf = input("Digite o CPF do funcionário (apenas números): ").strip()
        if len(cpf) == 11 and cpf.isdigit():
            if any(func.cpf == cpf for func in funcionarios):
                print("CPF já cadastrado!")
                continue
            break
        print("CPF inválido! Deve conter exatamente 11 dígitos numéricos.")

    cargo = input("Digite o cargo do funcionário: ")
    contrato = input("Digite o tipo de contrato do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    novo_funcionario = Funcionario(nome, idade, cpf, cargo, contrato, setor)
    funcionarios.append(novo_funcionario)
    print("Funcionário cadastrado com sucesso!")

def listar_funcionario():
    for func in funcionarios:
        if not funcionarios:
            print("Nenhum funcionário cadastrado!")

        else:
            print(func)
            print("\n")
            print("-" * 40)
            print(f'A lista possui {len(funcionarios)} funcionários.')
            print("-" * 40)
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
            confirmacao = input("Deseja realmente excluir o funcionário? (S/N): ")
            if confirmacao.upper() == "S":
                funcionarios.remove(func)
                return f'Funcionário {func.nome} removido com sucesso!'
            
            else:
                return f'Operação cancelada!'
        
        else:
            print("Funcionário não encontrado!")
    return None

opcao = 0
menu = True
funcionarios = []

def exibir_menu():
    while True:
        print(f'''
    {"-" * 40}MENU{"-" * 40}
            1 - Cadastrar Funcionário
            2 - Listar Funcionários
            3 - Buscar Funcionário
            4 - Excluir Funcionário
            5 - Sair
    ''')
        
        try:
            opcao = int(input("Escolha uma opção: "))

        except ValueError:
            print("Digite apenas números!")
            exibir_menu()
            
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
exibir_menu()