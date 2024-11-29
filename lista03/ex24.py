class Elevador:
    def __init__(self, total_andares):
        self.andar_atual = 0
        self.total_andares = total_andares

    def subir(self):
        if self.andar_atual < self.total_andares - 1:
            self.andar_atual += 1
        else:
            print('Já está no último andar.')

    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
        else:
            print('Já está no térreo.')

elevador = Elevador(10)
elevador.subir()  # Sobe para o andar 1
elevador.subir()  # Sobe para o andar 2
elevador.descer()  # Desce para o andar 1

print(f'Andar atual: {elevador.andar_atual}')
