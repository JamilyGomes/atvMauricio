class veiculo:
    def __init__(self,modelo, velocidade):
        self.modelo=modelo
        self.velocidade=velocidade 

    def aumento_Velo(self, incremento):
        incremento+=self.velocidade
        print("model :",self.modelo,'\nvel. anterior:',self.velocidade,"\nvel. atual :",incremento)

x=veiculo("Parati",80)
x.aumento_Velo(20)
