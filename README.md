# Gerenciador de Tarefas em Python

Este projeto é um simples gerenciador de tarefas em Python, dividido em três módulos: manipulação de dados, interface do usuário, e o arquivo principal que coordena a execução do programa.

## Estrutura do Projeto

- **`manipulacao_dados.py`**: Este módulo contém todas as funções relacionadas à manipulação de dados, como adicionar, listar, remover e marcar tarefas como concluídas.
- **`interface_usuario.py`**: Este módulo gerencia a interação do usuário com o sistema, exibindo menus, capturando entradas e chamando as funções apropriadas do módulo de manipulação de dados.
- **`main.py`**: O arquivo principal que coordena o fluxo do programa, utilizando a interface do usuário para interagir com as funções de manipulação de dados.

## Funcionalidades

1. **Adicionar Tarefa**:
   - Adiciona uma nova tarefa com a data de criação.
   - A tarefa é armazenada em um arquivo de texto (`tarefas.txt`).

2. **Listar Tarefas**:
   - Exibe todas as tarefas armazenadas, junto com suas datas de criação e, se aplicável, a data de conclusão.

3. **Remover Tarefa**:
   - Remove uma tarefa específica com base no índice fornecido pelo usuário.

4. **Marcar Tarefa como Concluída**:
   - Permite marcar uma tarefa como concluída, adicionando a data de conclusão.

5. **Persistência de Dados**:
   - As tarefas são armazenadas em um arquivo de texto (`tarefas.txt`), garantindo que as informações persistam entre as execuções do programa.

## Como Executar

1. **Clone este repositório**:
   ```bash
   git clone git@github.com:PenhaJV/gerenciador-de-tarefas.git
   ```

2. **Navegue até o diretório do projeto**:
   ```bash
   cd gerenciador-de-tarefas
   ```

3. **Execute o arquivo `main.py`**:
   ```bash
   python main.py
   ```

## Estrutura de Arquivos

```
gerenciador-de-tarefas/
│
├── main.py                # Arquivo principal que executa o programa
├── manipulacao_dados.py   # Módulo de manipulação de dados
└── interface_usuario.py   # Módulo de interface do usuário
```

## Explicação dos Módulos

### 1. `manipulacao_dados.py`

Este módulo contém as funções principais para gerenciar as tarefas:

- **`data_inicial()`**: Retorna a data atual no formato `dd/mm/yyyy`.
- **`data_final()`**: Retorna a data atual no formato `dd/mm/yyyy`.
- **`adicionar_tarefa(add_tarefa)`**: Adiciona uma nova tarefa ao arquivo `tarefas.txt` com a data de criação.
- **`listar_tarefas()`**: Retorna todas as tarefas armazenadas no arquivo.
- **`remover_tarefa(indice)`**: Remove uma tarefa específica com base no índice fornecido.
- **`marcar_tarefa_como_concluida(indice)`**: Marca uma tarefa como concluída e adiciona a data de conclusão.

### 2. `interface_usuario.py`

Este módulo lida com a interação do usuário:

- **`exibir_menu()`**: Exibe o menu principal e captura a escolha do usuário.
- **`adicionar_tarefa_interface()`**: Captura a entrada do usuário para adicionar uma nova tarefa.
- **`listar_tarefas_interface()`**: Exibe todas as tarefas armazenadas.
- **`remover_tarefa_interface()`**: Captura o índice da tarefa a ser removida e chama a função de remoção.
- **`marcar_tarefa_como_concluida_interface()`**: Captura o índice da tarefa a ser marcada como concluída e chama a função apropriada.

### 3. `main.py`

Este é o arquivo principal que coordena a execução do programa. Ele chama as funções da interface do usuário para interagir com o módulo de manipulação de dados, baseado nas escolhas do usuário.

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum bug ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
