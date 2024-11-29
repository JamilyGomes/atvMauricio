
class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    def calc_area(self):
        return self.lado ** 2
    def calc_perimetro(self):
        return 4 * self.lado
x = Quadrado(7)
print("A área do quadrado é: ", x.calc_area())
print("O perímetro do quadrado é:", x.calc_perimetro())
