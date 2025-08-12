from funcionario import *

def cadastrar_funcionario():
    cargo = input(f'''
{"-" * 40}CARGOS{"-" * 40}
        1 - Gerente
        2 - Vendedor
        3 - Jovem Aprendiz
        4 - Estagiário
        5 - Outro

        Digite o número do cargo: ''')
    nome =  input("Digite o nome do funcionário: ")

    while True:
        try:
            idade = int(input("Digite a idade do funcionário: "))
            if 18 <= idade <= 80:
                break
            print("Idade inválida! Deve estar entre 18 e 80 anos.")
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

    contrato = input("Digite o tipo de contrato do funcionário: ")
    setor = input("Digite o setor do funcionário: ")

    if cargo == "1":
        login = input("Digite o Login do gerente: ")
        senha = input("Digite a senha do gerente: ")
        while True:
            try:
                bonus_anual = float(input("Digite o bônus anual do gerente: R$"))
                break
            except ValueError:
                print("Valor inválido! Digite apenas números.")
        novo_funcionario = Gerente(nome, idade, cpf, "Gerente", contrato, setor, login, senha, bonus_anual)
        
    elif cargo == "2":
        novo_funcionario = Vendedor(nome, idade, cpf, "Vendedor", contrato, setor)

    elif cargo == "3":
        novo_funcionario = Jovem_aprendiz(nome, idade, cpf, "Jovem Aprendiz", contrato, setor)

    elif cargo == "4":
        novo_funcionario = Estagiario(nome, idade, cpf, "Estagiário", contrato, setor)

    elif cargo == "5":
        cargo_nome = input("Digite o cargo do funcionário: ")
        novo_funcionario = Funcionario(nome, idade, cpf, cargo_nome, contrato, setor)

    else: 
        print("Cargo inválido!")
        return
    
    funcionarios.append(novo_funcionario)
    print("Funcionário cadastrado com sucesso!")

def listar_funcionario():
    if not funcionarios:
        print("Nenhum funcionário cadastrado!")
        return

    for func in funcionarios:
        print(func)
        print("-" * 20)
    
    print("-" * 40)
    print(f'A lista possui {len(funcionarios)} funcionários.')
    print("-" * 40)
    print("Fim da lista de Funcionários")

def buscar_funcionario():
    cpf = input("Digite o cpf do funcionario que deseja buscar:")
    for func in funcionarios:
        if func.cpf == cpf:
            print("\n--- Funcionário Encontrado ---")
            print(func)
            print("-----------------------------\n")
            print("O que deseja fazer agora?")

            if isinstance(func, Gerente):
                op = input(f'''
{"-" * 40}OPÇÕES DE GERENTE{"-" * 40}
    1 - Delegar tarefa
    2 - Aprovar despesa
    Digite a opção desejada: ''')
                if op == "1":
                    tarefa = input("Digite a tarefa que precisa atribuir: ")
                    cpf_subordinado = input("Digite o CPF do subordinado: ")
                    subordinado_encontrado = None
                    for subordinado in funcionarios:
                        if subordinado.cpf == cpf_subordinado:
                            subordinado_encontrado = subordinado
                            break
                    if subordinado_encontrado:
                        func.delegar_tarefa(subordinado_encontrado, tarefa)
                    else:
                        print("Subordinado não encontrado!")

                elif op == "2":
                    try:
                        valor = float(input("Digite o valor da despesa: R$"))
                        func.aprovar_despesa(valor)
                    except ValueError:
                        print("Valor inválido. Digite um número.")

            elif isinstance(func, Vendedor):
                op = input(f'''
{"-" * 40}OPÇÕES DE VENDEDOR{"-" * 40}
    1 - Registrar venda
    2 - Calcular comissão
    Digite a opção desejada: ''')
                if op == "1":
                    try:
                        valor_venda = float(input("Digite o valor da venda: R$"))
                        func.registrar_venda(valor_venda)
                    except ValueError:
                        print("Valor inválido. Digite um número.")
                elif op == "2":
                    try:
                        percentual = float(input("Digite o percentual da comissão (%): "))
                        func.calcular_comissao(percentual)
                    except ValueError:
                        print("Percentual inválido. Digite um número.")
            
            elif isinstance(func, Jovem_aprendiz):
                op = input(f'''
{"-" * 40}OPÇÕES DE JOVEM APRENDIZ{"-" * 40}
    1 - Participar de treinamento
    2 - Auxiliar setor 
    Digite a opção que deseja: ''')
                if op == "1":
                    nome_curso = input("Digite o nome do curso: ")
                    func.participar_treinamento(nome_curso)
                elif op == "2":
                    func.auxiliar_setor()

            elif isinstance(func, Estagiario):
                op = input(f'''
{"-" * 40}OPÇÕES DE ESTAGIÁRIO{"-" * 40}
    1 - Entregar relatório
    2 - Aprender habilidade
    Digite a opção que deseja: ''')
                if op == "1":
                    nome_relatorio = input("Digite o nome do relatório: ")
                    func.entregar_relatorio(nome_relatorio)
                elif op == "2":
                    habilidade = input("Digite a habilidade que o estagiário aprendeu: ")
                    func.aprender_habilidade(habilidade)
            
            return
            
    print("Funcionário não encontrado!")

def excluir_funcionario():
    cpf = input("Digite o CPF do funcionário que deseja excluir: ")
    for func in funcionarios:
        if func.cpf == cpf:
            confirmacao = input(f"Deseja realmente excluir o funcionário {func.nome}? (S/N): ")
            if confirmacao.upper() == "S":
                funcionarios.remove(func)
                print(f'Funcionário {func.nome} removido com sucesso!')
            else:
                print('Operação cancelada!')
            return
            
    print("Funcionário não encontrado!")

def exibir_menu():
    while True:
        print(f'''
    {"-" * 40}MENU{"-" * 40}
            1 - Cadastrar Funcionário
            2 - Listar Funcionários
            3 - Buscar Funcionário e interagir
            4 - Excluir Funcionário
            5 - Sair
    ''')
        
        try:
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
                break
            else:
                print("Opção inválida! Tente novamente.")
        
        except ValueError:
            print("Opção inválida! Digite apenas números!")

if __name__ == "__main__":
    funcionarios = []
    exibir_menu()