# main.py

from task_manager import adicionar_tarefa, listar_tarefas, remover_tarefa

def mostrar_menu():
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")

def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tarefa = input("Digite a tarefa: ")
            adicionar_tarefa(tarefa)
        elif escolha == "2":
            listar_tarefas()
        elif escolha == "3":
            try:
                numero = int(input("Digite o número da tarefa a remover: "))
                remover_tarefa(numero)
            except ValueError:
                print("Por favor, digite um número válido.")
        elif escolha == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
