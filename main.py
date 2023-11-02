class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def comer(self, alimento):
        print(f"{self.nome} está comendo {alimento}")





p1 = Pessoa
p1.comer('pao')
