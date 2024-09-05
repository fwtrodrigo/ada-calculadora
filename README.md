> **Este projeto foi criado como parte do exercício prático do curso DevOps oferecido pela AdaTech.**

# Calculadora

Este é um exemplo simples de uma calculadora em Python que realiza operações básicas: adição, subtração, multiplicação e divisão.

## Funcionalidades

- Adição (`+`)
- Subtração (`-`)
- Multiplicação (`*`)
- Divisão (`/`)
- Opção para sair do programa (`9`)

## Requisitos

- Python 3.x

## Executando a Calculadora

1. **Clone o repositório**

2. **Abra um terminal**

3. **Execute o script**:

    ```bash
    cd ada-calculadora
    python app.py
    ```

## Como Usar

1. Ao executar o script, o programa pedirá para você inserir o símbolo da operação desejada:
    - `+` para adição
    - `-` para subtração
    - `*` para multiplicação
    - `/` para divisão
    - `9` para sair do programa

2. Após selecionar a operação, insira o primeiro e o segundo número quando solicitado.

3. O resultado da operação será exibido.

4. Para sair do programa, insira `9` quando solicitado para escolher a operação.

## Exemplos

- Para somar 5 e 3:
    ```plaintext
    Informe o simbolo referente a operacao desejada ('+', '-', '*', '/') ou '9' para sair do programa: +
    Informe o primeiro numero: 5
    Informe o segundo numero: 3
    Resultado: 8
    ```

- Para dividir 10 por 2:
    ```plaintext
    Informe o simbolo referente a operacao desejada ('+', '-', '*', '/') ou '9' para sair do programa: /
    Informe o primeiro numero: 10
    Informe o segundo numero: 2
    Resultado: 5.0
    ```

## Observações

- Se uma operação inválida for inserida, o programa solicitará novamente a operação desejada.
- Se for inserido um valor não numérico, o programa pedirá que um número válido seja inserido.
- A divisão por zero resultará em um erro e o programa exibirá uma mensagem informando que a divisão por zero não é permitida.