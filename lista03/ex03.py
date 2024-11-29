class Car:
    def __init__(self,modelo,ano):
        self.modelo=modelo
        self.ano=ano
    def __str__(self):
        print('modelo:',self.modelo,'\nano:',self.ano)
    
x=Car("gol","2023")
x.__str__()