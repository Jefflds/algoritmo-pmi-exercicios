# Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N

def main():
    try:
        n = int(input("Informe um número inteiro positivo: "))
        if n <= 0:
            print("Número inválido. Informe um número inteiro positivo.")
            return
    except ValueError:
        print("Entrada inválida. Informe um número inteiro.")
        return

    soma = 0.0
    for i in range(1, n + 1):
        soma += 1 / i

    print(f"A soma da série até 1/{n} é {soma:.2f}.")

main()