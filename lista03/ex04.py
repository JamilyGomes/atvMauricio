class Livro:
    def __init__(self, titulo, autor):
       self.titulo = titulo
       self.autor = autor
 
    def detalhes(self):

       print(f'Título: {self.titulo}, \nAutor: {self.autor}')
 
# Instanciar objeto

x = Livro('biblioteca da meia noite', 'Matt Haig')

x.detalhes()