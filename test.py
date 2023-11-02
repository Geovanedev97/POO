class ContaBancaria:
    def __init__(self, saldo_inicial, limite_cheque_especial):
        self.saldo = saldo_inicial
        self.limite_cheque_especial = limite_cheque_especial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} efetuado com sucesso. Saldo atual: R${self.saldo:.2f}')
        else:
            print('O valor do depósito deve ser maior que zero.')

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R${valor} efetuado com sucesso. Saldo atual: R${self.saldo:.2f}')
            else:
                if valor <= (self.saldo + self.limite_cheque_especial):
                    self.saldo -= valor
                    print(f'Saque de R${valor} efetuado com sucesso com uso do limite do cheque especial. Saldo atual: R${self.saldo:.2f}')
                else:
                    print('Saldo insuficiente.')
        else:
            print('O valor do saque deve ser maior que zero.')

    def obter_saldo(self):
        return self.saldo

