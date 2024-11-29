
class Calc_:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

calc = Calc_()
result_soma = calc.somar(10, 30)
print("Resultado soma: ", result_soma)

result_sub = calc.subtrair(21, 7)
print("Resultado da subtração: ", result_sub)
