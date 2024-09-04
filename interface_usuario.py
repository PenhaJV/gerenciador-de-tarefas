from manipulacao_dados import *

# Função para exibir o menu e obter a escolha do usuário


def exibir_menu():
    print("\nMenu de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Marcar Tarefa como Concluída")
    print("5. Sair")
    return input("Escolha uma opção: ")


# Função para adicionar uma tarefa
def adicionar_tarefa_interface():
    tarefa = input("Digite a tarefa a ser adicionada: ")
    adicionar_tarefa(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso.")


# Função para listar tarefas
def listar_tarefas_interface():
    tarefas = listar_tarefas()
    if tarefas:
        for indice, tarefa in enumerate(tarefas):
            print(f"{indice} - {tarefa.strip()}")
    else:
        print("Nenhuma tarefa encontrada.")


# Função para remover uma tarefa
def remover_tarefa_interface():
    listar_tarefas_interface()
    entrada = int(
        input("Qual tarefa gostaria de remover (digite o número correspondente): "))
    tarefa_removida = remover_tarefa(entrada)
    if tarefa_removida:
        print(f"Tarefa '{tarefa_removida}' removida com sucesso.")
    else:
        print("Número inválido.")


# Função para marcar uma tarefa como concluída
def marcar_tarefa_como_concluida_interface():
    listar_tarefas_interface()
    entrada = int(input(
        "Qual tarefa gostaria de marcar como concluída (digite o número correspondente): "))
    tarefa_concluida = marcar_tarefa_como_concluida(entrada)
    if tarefa_concluida:
        print(f"Tarefa '{tarefa_concluida}' marcada como concluída.")
    else:
        print("Número inválido.")
