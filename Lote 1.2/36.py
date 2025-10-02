# Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num - 1)

def main():
    try:
        n = int(input("Informe um número inteiro N: "))
        if n < 0:
            print("Por favor, informe um número inteiro não negativo.")
            return
    except ValueError:
        print("Entrada inválida. Informe um número inteiro.")
        return

    serie = sum(1 / fatorial(i) for i in range(n + 1))

    print(f"O resultado da série 1 + 1/1! + 1/2! + ... + 1/{n}! é {serie:.6f}")
main()
