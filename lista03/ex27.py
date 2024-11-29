
class Animal:
    def __init__(self, especie):
        self.especie = especie

    def mover(self):
        if self.especie == "peixe":
            print("O peixe nada.")
        elif self.especie == "pássaro":
            print("O pássaro voa.")
        elif self.especie == "cachorro":
            print("O cachorro corre.")
        elif self.especie == "preguiça":
            print("a preguiça dorme.")
        else:
            print("O {self.especie} se move de uma forma desconhecida.")

peixe = Animal("peixe")
passaro = Animal("pássaro")
cachorro = Animal("cachorro")
gato = Animal("preguiça")

peixe.mover()     
passaro.mover()    
cachorro.mover()   
gato.mover()       
