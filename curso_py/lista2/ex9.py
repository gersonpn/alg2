class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def deposito(self, x):
        if x <= 0:
            return "Valor inválido"
        else:
            self.saldo += x
            return f"Depósito efetuado, R${x}"

    def saque(self, y):
        if y <= 0:
            return "Valor inválido"
        elif y > self.saldo:
            return "Saldo insuficiente"
        else:
            self.saldo -= y
            return f"Saque efetuado, R${y}"

    def transferência(self, outra_conta, x):
        if x <= 0:
            return "Valor inválido"
        elif x > self.saldo:
            return "Saldo insuficiente"
        else:
            self.saldo -= x
            outra_conta.saldo += x
            return "Transferência efetuada com sucesso"



conta = ContaBancaria(90.50)
print(conta.deposito(33.50))
print('saldo R$', conta.saldo)