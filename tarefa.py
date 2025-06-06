
class Tarefa:
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade

    def __str__(self):
        return f"Nome: {self.nome} - Prioridade: {self.prioridade}"
