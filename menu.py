
import gerenciador


def exibir_menu():
    while True:
        print("Menu:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome da tarefa: ")
            print("Selecione a prioridade: \n1. Alta\n2. Média\n3. Baixa")
            opcao_prioridade = input("Escolha uma prioridade: ")
            prioridade = {"1": "Alto", "2": "Médio",
                          "3": "Baixo"}.get(opcao_prioridade, "Baixo")
            gerenciador.adicionar_tarefa(nome, prioridade)
        elif opcao == "2":
            gerenciador.listar_tarefas()
        elif opcao == "3":
            gerenciador.listar_tarefas()
            try:
                indice = int(
                    input("Digite o índice da tarefa a ser concluída: ")) - 1
                gerenciador.concluir_tarefa(indice)
            except ValueError:
                print("Entrada inválida! Por favor, insira um número.")
        elif opcao == "4":
            gerenciador.listar_tarefas()
            try:
                indice = int(
                    input("Digite o índice da tarefa a ser removida: ")) - 1
                gerenciador.excluir_tarefa(indice)
            except ValueError:
                print("Entrada inválida! Por favor, insira um número.")
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")
