class Carro:
    def __init__(self, marca, combustivel):
        self.marca = marca
        self.combustivel = combustivel

    def abastecer(self, quantidade):
        if quantidade > 0:
            self.combustivel += quantidade
            print(f"Abastecendo... \nNovo nível de combustível: {self.combustivel} litros.")
        else:
            print("Quantidade de combustível inválida. O valor deve ser positivo.")

    def verificar_combustivel(self):
        print(f"Nível de combustível: {self.combustivel} litros.")

    def __str__(self):
        return f"Carro {self.marca} - \nCombustível: {self.combustivel} litros"

carro = Carro("Fusca", 20)
carro.verificar_combustivel()
carro.abastecer(15)
carro.verificar_combustivel()

print(carro)
