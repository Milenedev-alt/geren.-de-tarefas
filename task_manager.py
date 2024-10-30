# task_manager.py

def adicionar_tarefa(tarefa):
    with open("tasks.txt", "a") as arquivo:
        arquivo.write(tarefa + "\n")
    print("Tarefa adicionada com sucesso!")


def listar_tarefas():
    try:
        with open("tasks.txt", "r") as arquivo:
            tarefas = arquivo.readlines(
            if tarefas:
                print("Suas tarefas:")
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i}. {tarefa.strip()}")
            else:
                print("Nenhuma tarefa encontrada.")
    except FileNotFoundError:
        print("Nenhuma tarefa encontrada.")


def remover_tarefa(numero):
    try:
        with open("tasks.txt", "r") as arquivo:
            tarefas = arquivo.readlines()
        
        if 0 < numero <= len(tarefas)
            del tarefas[numero - 1]
            with open("tasks.txt", "w") as arquivo:
                arquivo.writelines(tarefas)
            print("Tarefa removida com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except FileNotFoundError:
        print("Nenhuma tarefa para remover.")
