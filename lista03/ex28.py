
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f'{self.titular}: R${self.saldo:.2f}' 

class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_saldos(self):
        if not self.contas:
            print("Não há contas cadastradas no banco.")
            return
        print("Saldos das contas:")
        for conta in self.contas:
            print(conta)

banco = Banco()

# Add contas ao banco
x = ContaBancaria("Arnaldo", 1000)
x1 = ContaBancaria("Joseph", 2000)
x2 = ContaBancaria("Lucas", 1500)

banco.adicionar_conta(x)
banco.adicionar_conta(x1)
banco.adicionar_conta(x2)

banco.listar_saldos()
