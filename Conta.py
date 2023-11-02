class Conta:
    def __init__(self, numero, nome, tipo):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.saldo = 0
        self.limite = 0
        self.status = False
    def ativarconta(self):
        if self.status == False:
            self.status = True
            print("Sua conta foi ativada")
        else:
            print("Sua conta já está ativa")
    def desativar_conta(self):
        if self.saldo != 0 and self.status == True:
            print("Saque seu saldo, para desativar sua conta")
        elif self.saldo == 0 and self.status == True:
            print("Conta desativada")
            self.status = False
        else:
            print("sua conta já está desativada")
    def ativar_limite(self, valor_limite):
        if self.status == False:
            print("Sua conta está desativada")
        elif self.limite == 0:
            self.limite = valor_limite
            print(f"Adicionado limite de R${self.limite}")
        else:
            print("O limite da conta já foi ativado")
    def depositar(self, valor_deposito):
        if self.status == False:
            print("Sua conta está desativada")
        elif valor_deposito > 0:
            self.saldo += valor_deposito
            print(f"R${valor_deposito} depositado com sucesso.")
            self.status = True
        else:
            print("O valor deverá ser maior que 0!")
    def sacar(self, valor):
        if self.status == False:
            print("Sua conta está desativada")
        elif valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor} efetuado com sucesso. Saldo atual: R${self.saldo}")
            else:
                if valor <= (self.saldo + self.limite):
                    self.saldo -= valor
                    print(f"Saque de R${valor} efetuado com sucesso do limite do cheque especial. Saldo atual: R${self.saldo}")
                else:
                    print("Saldo insuficiente.")
        else:
            print("O valor do saque deve ser maior que zero.")
    def verificarsaldo(self):
        if self.status == False:
            print("Sua conta está desativada")
        else:
            print(f"O seu saldo é de: R${self.saldo}")
