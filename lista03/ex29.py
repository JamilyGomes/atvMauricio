class Game:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0

    def iniciar_jogo(self):
        print(f"Iniciando jogo {self.nome}...")

    def registrar_pontuacao(self, pontos):
        if pontos > 0:
            self.pontuacao += pontos
            print(f"Pontos registrados: {pontos}")
        else:
            print("A pontuação deve ser positiva.")

    def exibir_pontuacao(self):
        print(f"Pontos atual: {self.pontuacao}.")

# Usando a classe Jogo
jogo = Game("Donkey Kong")
jogo.iniciar_jogo()
jogo.registrar_pontuacao(10)
jogo.registrar_pontuacao(20)
jogo.exibir_pontuacao()




