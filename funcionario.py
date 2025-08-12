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
        # Aqui você poderia adicionar validações, como não permitir nomes vazios
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
        # Exemplo de validação: idade deve ser um número positivo
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
        # Exemplo de validação: verificar se o CPF tem 11 dígitos (simplificado)
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
        # Note que aqui usamos os getters (self.nome, self.idade, etc.)
        # para acessar os valores, o que é uma boa prática.
        return f'''
    nome: {self.nome}
    idade: {self.idade}
    cpf: {self.cpf}
    cargo: {self.cargo}
    contrato: {self.contrato}
    setor: {self.setor}
    '''

# Exemplo de uso:
funcionario1 = Funcionario("João da Silva", 30, "12345678901", "Desenvolvedor", "CLT", "Tecnologia")

# Usando o getter para obter o nome
print(f"Nome original: {funcionario1.nome}")

# Usando o setter para alterar o nome
funcionario1.nome = "João de Souza"
print(f"Nome alterado: {funcionario1.nome}")

# Tentando atribuir um valor inválido para a idade (o setter irá bloquear)
funcionario1.idade = -5
print(f"Idade (após tentativa de alteração inválida): {funcionario1.idade}")


# Exibindo o objeto completo
print("\nDados do Funcionário:")
print(funcionario1)

class Gerente(Funcionario):
    def __init__(self, nome, idade, cpf, cargo, contrato, setor, login, senha):
        super().__init__(nome, idade, cpf, cargo, contrato, setor)    
        self.login = login
        self.senha = senha
    
    def login_gerente(self, login, senha):
        self.login = input("Usuario:")
        self.senha = input("Senha:")
        if self.login == login and self.senha == senha:
            return True
        else:
            return False
        
    def aumento(self):
        if self.login_gerente() == True:
           pass

class Vendedor(Funcionario):
    def __init__(self, nome, idade, cpf, cargo, contrato, setor):
        super().__init__(nome, idade, cpf, cargo, contrato, setor)
        
class jovem_aprendiz(Funcionario):
    def __init__(self, nome, idade, cpf, cargo, contrato, setor):
        super().__init__(nome, idade, cpf, cargo, contrato, setor)
        
class estagiario(Funcionario):
    def __init__(self, nome, idade, cpf, cargo, contrato, setor):
        super().__init__(nome, idade, cpf, cargo, contrato, setor)
    

        
