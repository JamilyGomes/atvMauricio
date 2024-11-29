class People:

    def __init__(self, nome, altura):
       self.nome = nome
       self.altura = altura
 
    def ver_altura(self):
       if self.altura > 1.75:
            print(f'{self.nome} é mais alto(a) que 1,75 m.')
       else:
            print(f'{self.nome} não é mais alto(a) que 1,75 m.')
 
# Usando a classe Pessoa
x = People('Mily', 1.45)
x.ver_altura()