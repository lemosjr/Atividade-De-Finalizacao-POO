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
        