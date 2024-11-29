class P:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
    

    def exibir(self):
        print('nome:',self.nome,'\nidade:',self.idade)
        
y=P("Betta",21)
y.exibir()