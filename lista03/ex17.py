
class Data:
    def __init__(self,dia,mes,ano):
        self.dia=dia
        self.mes=mes
        self.ano=ano
        
    def exibir(self):
        print(self.dia,self.mes,self.ano,sep="/")
x=Data(10,12,2024)
x.exibir()
