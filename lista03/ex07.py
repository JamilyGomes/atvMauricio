class P:
    def __init__(self,nome,preco):
        self.nome=nome
        self.preco=preco
    def desconto(self):
        Vdesc=0.05
        valorFinal=self.preco-(self.preco*Vdesc)
        return valorFinal
       
    
x=P("desodorante",14.99)
y=P("sabonete",1.40)
print("Valor com desconto:", x.desconto())
print("Valor com desconto:",y.desconto())
