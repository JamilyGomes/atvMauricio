
class Livro:
    def __init__(self, titulo, autor, estoque):
        self.titulo = titulo  
        self.autor = autor
        self.estoque = estoque 

    def ver_estoque(self):
        return self.estoque
    
    def vender_livro(self, quantidade=1):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
            print(quantidade,' livro(s) de ',self.titulo,' vendido(s). Estoque restante:',self.estoque)
        else:
            print(f"Estoque insuficiente para vender {quantidade} livro(s). Estoque atual: {self.estoque}.")

x = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 10)
print('Estoque de ',x.titulo,':',x.ver_estoque())

x.vender_livro(4)
x.vender_livro(9) 
