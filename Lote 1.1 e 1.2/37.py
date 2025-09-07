#  Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    try:
        n = int(input("Informe um número inteiro N: "))
        if n < 0:
            print("Por favor, informe um número inteiro não negativo.")
            return
    except ValueError:
        print("Entrada inválida. Informe um número inteiro.")
        return

    print("Série de Fibonacci:")
    for i in range(n + 1):
        print(fibonacci(i), end=" ")

    print()

main()