class Funcionario:
    def __init__(self, nome, idade, cpf, cargo, contrato, setor):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._cargo = cargo
        self._contrato = contrato
        self._setor = setor

    # Getter para 'nome'
    @property
    def nome(self):
        return self._nome

    # Setter para 'nome'
    @nome.setter
    def nome(self, novo_nome):
        if novo_nome and isinstance(novo_nome, str):
            self._nome = novo_nome
        else:
            print("Erro: Nome inválido.")

    # Getter para 'idade'
    @property
    def idade(self):
        return self._idade

    # Setter para 'idade'
    @idade.setter
    def idade(self, nova_idade):
        if isinstance(nova_idade, int) and nova_idade > 0:
            self._idade = nova_idade
        else:
            print("Erro: Idade inválida.")

    # Getter para 'cpf'
    @property
    def cpf(self):
        return self._cpf

    # Setter para 'cpf'
    @cpf.setter
    def cpf(self, novo_cpf):
        if isinstance(novo_cpf, str) and len(novo_cpf) == 11:
            self._cpf = novo_cpf
        else:
            print("Erro: CPF inválido. Deve conter 11 dígitos.")

    # Getter para 'cargo'
    @property
    def cargo(self):
        return self._cargo

    # Setter para 'cargo'
    @cargo.setter
    def cargo(self, novo_cargo):
        self._cargo = novo_cargo

    # Getter para 'contrato'
    @property
    def contrato(self):
        return self._contrato

    # Setter para 'contrato'
    @contrato.setter
    def contrato(self, novo_contrato):
        self._contrato = novo_contrato

    # Getter para 'setor'
    @property
    def setor(self):
        return self._setor

    # Setter para 'setor'
    @setor.setter
    def setor(self, novo_setor):
        self._setor = novo_setor

    def __str__(self):
        return f'''
    nome: {self.nome}
    idade: {self.idade}
    cpf: {self.cpf}
    cargo: {self.cargo}
    contrato: {self.contrato}
    setor: {self.setor}
    '''

class Gerente(Funcionario):
    def __init__(self, nome, idade, cpf, cargo, contrato, setor, login, senha, bonus_anual):
        super().__init__(nome, idade, cpf, cargo, contrato, setor)      
        self.login = login
        self.senha = senha
        self.bonus_anual = bonus_anual

    def delegar_tarefa(self, funcionario, tarefa):
        print(f"O gerente {self.nome} delegou a tarefa '{tarefa}' para o funcionário {funcionario.nome}.")

    def aprovar_despesa(self, valor):
        if valor > 0 and valor <= self.bonus_anual:
            print(f"Gerente {self.nome} aprovou a despesa no valor de R${valor:.2f}.")
            return True
        else:
            print(f"Despesa de R${valor:.2f} não autorizada. Excede o limite ou é inválida.")
            return False

class Vendedor(Funcionario):
    def __init__(self, nome, idade, cpf, cargo, contrato, setor):
        super().__init__(nome, idade, cpf, cargo, contrato, setor)
        self.vendas = []

    def registrar_venda(self, valor_da_venda):
        if valor_da_venda > 0:
            self.vendas.append(valor_da_venda)
            print(f"Venda de R${valor_da_venda:.2f} registrada para o vendedor {self.nome}.")
        else:
            print("Valor da venda inválido.")

    def calcular_comissao(self, percentual_comissao):
        total_vendas = sum(self.vendas)
        comissao = total_vendas * (percentual_comissao / 100)
        print(f"A comissão do vendedor {self.nome} é de R${comissao:.2f} sobre um total de R${total_vendas:.2f} em vendas.")
        return comissao
        
class Jovem_aprendiz(Funcionario):
    def __init__(self, nome, idade, cpf, cargo, contrato, setor):
        super().__init__(nome, idade, cpf, cargo, contrato, setor)
        
    def participar_treinamento(self, nome_curso):
        print(f"O Jovem Aprendiz {self.nome} está participando do treinamento '{nome_curso}'.")

    def auxiliar_setor(self):
        print(f"{self.nome} está auxiliando nas tarefas gerais do setor de {self.setor}.")
        
class Estagiario(Funcionario):
    def __init__(self, nome, idade, cpf, cargo, contrato, setor):
        super().__init__(nome, idade, cpf, cargo, contrato, setor)
        
    def entregar_relatorio(self, nome_relatorio):
        print(f"O estagiário {self.nome} entregou o relatório: '{nome_relatorio}'.")

    def aprender_habilidade(self, habilidade):
        print(f"{self.nome}, do setor de {self.setor}, aprendeu a nova habilidade: '{habilidade}'.")
        