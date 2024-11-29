import math

class Circulo:
    def __init__(self,raio):
        self.raio=raio
      
    def __str__(self):

        return 2*math.pi*self.raio
    
y=Circulo(5)
print(y.__str__())



