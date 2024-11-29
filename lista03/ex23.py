class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_aumento(self, porc):
        if porc <= 0:
            print("Porcentagem de aumento deve ser positiva.")
            return
        aumento = self.salario * (porc / 100)
        self.salario += aumento
        return aumento

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Salário Atual: R${self.salario:.2f}')

f = Funcionario('Abel', 3000)

f.exibir_dados()

aumento = f.calcular_aumento(10)

if aumento:
    print(f'Aumento de R${aumento:.2f} concedido.')
    f.exibir_dados()
