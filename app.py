def calculator():
    print("Bem vindo a calculadora!")

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    while True:
        operation = get_operation()

        if operation == "9":
            quit_program()

        num1 = get_number("Informe o primeiro numero: ")
        num2 = get_number("Informe o segundo numero: ")

        try:
            result = operations[operation](num1, num2)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Erro: {e}")


def get_operation():
    while True:
        operation = input(
            "Informe o simbolo referente a operacao desejada ('+', '-', '*', '/') ou '9' para sair do programa: "
        )

        if operation not in ("+", "-", "*", "/", "9"):
            print("Operacao invalida. Favor, informe uma das opcoes apresentadas")
            continue

        return operation


def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Favor, digite um numero valido.")


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Nao é possivel dividir por zero.")
    return x / y


def quit_program():
    print("Programa finalizado!")
    exit()


if __name__ == "__main__":
    calculator()
