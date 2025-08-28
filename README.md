# Sistema de Gerenciamento de Funcionários (CLI)

## Visão Geral

Este projeto é um sistema de linha de comando (CLI) para gerenciamento de funcionários, desenvolvido em Python. A aplicação demonstra de forma prática os pilares da **Programação Orientada a Objetos (POO)**, como encapsulamento, herança e polimorfismo, para criar um sistema modular e expansível para cadastrar, listar, buscar, interagir e excluir funcionários de diferentes cargos.

-----

## Conceitos de POO Demonstrados

Este projeto foi estruturado para ser um exemplo claro da aplicação dos seguintes conceitos de POO:

  - **Encapsulamento**:

      - Os atributos da classe base `Funcionario` são protegidos (ex: `_nome`).
      - O acesso a esses atributos é controlado por meio de *getters* (`@property`) e *setters* (`@nome.setter`), que permitem a inclusão de lógicas de validação. Por exemplo, o CPF e a idade só podem ser alterados se atenderem a regras específicas.

  - **Herança**:

      - Uma classe base `Funcionario` define os atributos e comportamentos comuns a todos os funcionários.
      - Classes específicas como `Gerente`, `Vendedor`, `Jovem_aprendiz` e `Estagiario` herdam da classe `Funcionario`, reutilizando seu código e adicionando atributos e métodos próprios.

  - **Polimorfismo**:

      - O polimorfismo é claramente visível na funcionalidade "Buscar Funcionário e Interagir". Após encontrar um funcionário, o sistema verifica seu tipo (`isinstance`) e exibe um menu de ações específicas para aquele cargo.
      - Dessa forma, objetos de classes diferentes (Gerente, Vendedor, etc.) respondem de maneiras distintas à mesma chamada de "interação", executando métodos exclusivos de sua classe.

-----

## Funcionalidades

  - **Cadastro de Funcionários**: Permite adicionar novos funcionários, escolhendo entre diferentes cargos (Gerente, Vendedor, etc.).
  - **Sistema Baseado em Cargos**: Cada cargo possui funcionalidades e atributos únicos.
      - **Gerente**: Pode delegar tarefas e aprovar despesas.
      - **Vendedor**: Pode registrar vendas e calcular comissões.
      - **Jovem Aprendiz**: Pode participar de treinamentos e auxiliar o setor.
      - **Estagiário**: Pode entregar relatórios e aprender novas habilidades.
  - **Listagem Completa**: Exibe todos os funcionários cadastrados com seus respectivos detalhes.
  - **Busca e Interação**: Busca um funcionário pelo CPF e permite executar ações específicas do seu cargo.
  - **Exclusão de Funcionários**: Remove um funcionário do sistema de forma segura, com confirmação.
  - **Validação de Entradas**: Garante que dados como CPF e idade sejam inseridos no formato correto.

-----

## Estrutura do Projeto

  - `funcionario.py`: Contém a definição da classe base `Funcionario` e de todas as classes que herdam dela (`Gerente`, `Vendedor`, etc.). É o módulo que define o modelo de dados e o comportamento dos objetos.
  - `main.py`: É o ponto de entrada da aplicação. Contém a lógica da interface de linha de comando (o menu), as funções para interagir com o usuário (cadastrar, listar, etc.) e o loop principal do programa.

-----

## Como Executar

Este projeto não requer a instalação de bibliotecas externas, apenas o **Python 3.x**.

1.  **Baixe os arquivos**:
    Certifique-se de que os arquivos `funcionario.py` e `main.py` estejam na mesma pasta.

2.  **Abra o terminal**:
    Navegue pelo terminal até o diretório onde você salvou os arquivos.

3.  **Execute o comando**:
    Rode o arquivo `main.py` para iniciar o sistema.

    ```bash
    python main.py
    ```

4.  **Navegue pelo menu**:
    O sistema exibirá um menu interativo. Digite o número da opção desejada para utilizar as funcionalidades.