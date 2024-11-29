class Aluno:

    def __init__(self, nome, nota):
       self.nome = nome
       self.nota = nota
 
    def ver_aprov(self):
       if self.nota >= 7:
            print(f'{self.nome} aprovada.')

       else:
            print(f'{self.nome} reprovada.')
 
# Instanciando um objeto
x = Aluno('Jamily:', 7.5)
x.ver_aprov()
