class Eletrodomestico:
    def __init__(self, nome, pot):
        
        self.nome = nome
        self.pot = pot

    def ligar(self):
    
        print("O " + self.nome + " de " + str(self.pot) + "W foi ligada.")


y = Eletrodomestico("maquina de lavar", 250)


y.ligar()
