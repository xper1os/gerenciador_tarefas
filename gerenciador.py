
from tarefa import Tarefa

tarefas = []


def prioridade_valor(prioridade):
    return {
        1: "Alta",
        2: "Média",
        3: "Baixa"
    }.get(prioridade, 4)  # Retorna 0 se a prioridade não for reconhecida


def adicionar_tarefa(nome, prioridade):
    tarefas.append(Tarefa(nome, prioridade))
    print(f"Tarefa adicionada com sucesso!")


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada!")
    else:
        print("Tarefas")
        for i, tarefa in enumerate(sorted(tarefas, key=lambda x: prioridade_valor(x.prioridade)), start=1):
            print(f"{i}. {tarefa}")


def concluir_tarefa(indice):
    try:
        concluida = tarefas.pop(indice)
        print(f"Tarefa {concluida.nome} concluída com sucesso!")
    except IndexError:
        print("Tarefa não encontrada!")


def excluir_tarefa(indice):
    try:
        excluida = tarefas.pop(indice)
        print(f"Tarefa {excluida.nome} excluída com sucesso!")
    except IndexError:
        print("Tarefa não encontrada!")
