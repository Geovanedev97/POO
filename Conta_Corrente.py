class ContaCorrente:
    def __init__(self,numeroConta, nome, tipo_conta ):
        self.numeroconta = numeroConta
        self.saldo = 0
        self.status = False
        self.nome = nome
        self.tipo_conta = tipo_conta


    def ativar_conta(self):
        self.status = False


    def saque(self, novoSaldo):
        self.status = True
        if self.status == False:
            if self.saldo >= novoSaldo:
                self.saldo -= novoSaldo
            else:
                print(f"Saldo insuficente. Saldo: {self.saldo}")
        self.status = False
        if self.status == False and self.saldo == 0:
            print("Sua conta esta desativada")

    def Deposito(self, novoSaldo):
        if self.status == "ativo":
            if novoSaldo == 0:
                print("O valor deve ser maior que 0.")
            else:
                self.saldo += novoSaldo
        elif self.status == "desativar" and self.saldo == 0:
            print(f"{self.nome} sua conta está desativada")

    def ver_saldo(self):
        if self.status == "ativo" or self.saldo == 0:
            print(self.saldo)
        elif self.status == "desativar" and self.saldo == 0:
            print("Sua conta está desativada")

'''    def ativar_desativar(self,novo_status):
        self.status = novo_status
        while self.saldo != 0 and novo_status == "desativar":
            novo_status == "desativar"
            print("Seu saldo deverá está zerado para desativar")
            break
'''





