

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def c_area(self):
        return self.largura * self.altura

x = Retangulo(5, 10)

area = x.c_area()
print(f"área do retângulo é: {area}")
