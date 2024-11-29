class Calculadora:

    def __init__(self):
        self.historico = []

    def _registrar_operacao(self, operacao, a, b, resultado):
        self.historico.append(f'{operacao}: {a} {operacao} {b} = {resultado}')

    def somar(self, a, b):
        resultado = a + b
        self._registrar_operacao('Soma', a, b, resultado)
        return resultado

    def subtrair(self, a, b):
        resultado = a - b
        self._registrar_operacao('Subtração', a, b, resultado)
        return resultado

    def exibir_historico(self):
        for operacao in self.historico:
            print(operacao)

# Usando a classe Calculadora
calc = Calculadora()
calc.somar(10, 5)
calc.subtrair(10, 5)
calc.exibir_historico()



