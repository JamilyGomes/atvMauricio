class ConversorDeMoeda:
    def __init__(self,moeda):
        self.moeda=moeda
    def converter(self):
        dolar=5.77
        valor=self.moeda*dolar
        print("valor em dolares",self.moeda,"em reais:",valor)
y=ConversorDeMoeda(330)
y.converter()
