from datetime import datetime

# Funções para manipulação de datas


def data_inicial():
    return datetime.now().strftime("%d/%m/%Y")


def data_final():
    return datetime.now().strftime("%d/%m/%Y")

# Função para adicionar uma tarefa com data de criação


def adicionar_tarefa(add_tarefa):
    with open("tarefas.txt", "a") as nova_tarefa:
        nova_tarefa.write(f"{add_tarefa} - Criada em: {data_inicial()}\n")

# Função para listar todas as tarefas


def listar_tarefas():
    with open("tarefas.txt", "r") as arquivo:
        tarefas = arquivo.readlines()
    return tarefas

# Função para remover uma tarefa por índice


def remover_tarefa(indice):
    with open("tarefas.txt", "r") as arquivo:
        tarefas = arquivo.readlines()

    if 0 <= indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        with open("tarefas.txt", "w") as arquivo:
            arquivo.writelines(tarefas)
        return tarefa_removida.strip()
    else:
        return None

# Função para marcar uma tarefa como concluída


def marcar_tarefa_como_concluida(indice):
    with open("tarefas.txt", "r") as arquivo:
        tarefas = arquivo.readlines()

    if 0 <= indice < len(tarefas):
        tarefa = tarefas[indice].strip()
        tarefas[indice] = f"{tarefa} - Concluída em: {data_final()}\n"
        with open("tarefas.txt", "w") as arquivo:
            arquivo.writelines(tarefas)
        return tarefa
    else:
        return None
