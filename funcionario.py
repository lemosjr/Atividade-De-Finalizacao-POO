class Funcionario:
    def __init__(self, nome, idade, cpf, cargo, contrato, setor):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cargo = cargo
        self.contrato = contrato
        self.setor = setor
    
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
    def __init__(self, nome, idade, cpf, cargo, contrato, setor, login, senha):
        super().__init__(nome, idade, cpf, cargo, contrato, setor)    
        self.login = login
        self.senha = senha
    
    def login_gerente(self,login, senha):
        self.login = input("Usuario:")
        self.senha = input("Senha:")
        if self.login == login and self.senha == senha:
            return True
        else:
            return False
        
    def aumento(self):
        if self.login_gerente() == True:
           pass
            
            
funcionario = Funcionario("joao", 28, "12345678910", "gerente", "pj", "contabilidade")

print(funcionario)
    
    
    
        