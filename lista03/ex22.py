class Agenda:

    def __init__(self):
       self.contatos = []
 
    def adicionar_contato(self, nome, telefone):
       self.contatos.append({'nome': nome, 'telefone': telefone})
 
    def listar_contatos(self):
       for contato in self.contatos:

            print(f'Nome: {contato["nome"]}, Telefone: {contato["telefone"]}')
 
# Usando a classe Agenda
agnd = Agenda()
agnd.adicionar_contato('Dayane', '1234-5678')
agnd.adicionar_contato('Hugo', '9876-5432')
agnd.listar_contatos()


