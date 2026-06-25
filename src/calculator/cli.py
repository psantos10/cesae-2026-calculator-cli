import platform
import subprocess

from calculator import operations

def main() -> None:
    while True:
        operation = menu_selector()
        if operation == 0:
            break


        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        result = execute_operation(operation, num1, num2)
        print()
        print(f"Resultado: {result}")
        input("Pressione ENTER para continuar...")


    print("Até a próxima! 👋")



def menu_selector() -> int:
    clear_screen();
    print("=== CALCULADOR CLI - MENU ===")
    print()
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. SAIR")
    print()

    return int(input("Selecione uma opção (0-4): "))


def execute_operation(op: int, num1: float, num2: float) -> float:
    if op == 1:
        return operations.add(num1, num2)
    elif op == 2:
        return operations.subtract(num1, num2)
    elif op == 3:
        return operations.multiply(num1, num2)
    elif op == 4:
        return operations.divide(num1, num2)
    else:
        raise ValueError("Operação inválida!")


def clear_screen() -> None:
    command = "cls" if platform.system() == "Windows" else "clear"
    subprocess.run(command, shell=True, check=False)


if __name__ == "__main__":
    main()
