from interface_usuario import *

# Função principal para coordenar o programa


def main():
    while True:
        escolha = exibir_menu()

        if escolha == "1":
            adicionar_tarefa_interface()
        elif escolha == "2":
            listar_tarefas_interface()
        elif escolha == "3":
            remover_tarefa_interface()
        elif escolha == "4":
            marcar_tarefa_como_concluida_interface()
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Execução do programa
if __name__ == "__main__":
    main()
