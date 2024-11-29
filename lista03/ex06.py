
class Animal:
    def __init__(self, especie, som):
        self.especie = especie
        self.som = som

    def emitir_som(self):
        print(f'{self.especie} faz "{self.som}"')


pato=Animal("pato","Quà-Quá")

pato.emitir_som()