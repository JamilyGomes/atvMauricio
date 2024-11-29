class Pessoa:

    def __init__(self, nome, altura, peso):
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        classificacao = self.classificar_imc(imc)
        print(f'IMC de {self.nome}: {imc:.2f} - {classificacao}')

    def classificar_imc(self, imc):
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 39.9:
            return "Obesidade"
        else:
            return "Obesidade grave"

# Usando a classe Pessoa
p = Pessoa('Raquel', 1.62, 56)
p.calcular_imc()

# Exemplo com outro valor
p1 = Pessoa('Betta', 1.45, 50)
p1.calcular_imc()
