
class ContaBanc:
        def __init__(self, saldo_inic=0):
            self.saldo = saldo_inic
    
        def dep(self, valor):
            if valor > 0:
                self.saldo += valor
                print("Depósito de R$",valor," realizado com sucesso")
            else:
                print("Valor inválido")
    
        def sacar(self, valor):
            if valor > 0:
                if valor <= self.saldo:
                    self.saldo -= valor
                    print ("Saque de R$",valor," realizado com sucesso!")
                else:
                    print("Saldo insuficiente")
            else:
                print("Valor de saque inválido")
    

x=ContaBanc(10)
x.sacar(30)
x.dep(2)
