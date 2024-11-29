class Filme:
    def __init__(self, titulo, duracao):
    
        self.titulo = titulo
        self.duracao = duracao

    def exi_det(self):

        print("Título: " + self.titulo)
        print("Duração: " + str(self.duracao) + " hrs" )

filme = Filme("Vingadores Ultimato",3)

filme.exi_det()
