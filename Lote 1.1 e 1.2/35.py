# Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.

def main():
    try:
        num1 = int(input("Informe o primeiro número inteiro: "))
        num2 = int(input("Informe o segundo número inteiro: "))
    except ValueError:
        print("Entrada inválida. Informe números inteiros.")
        return

    maior = max(num1, num2)
    menor = min(num1, num2)

    soma_impares = sum(i for i in range(menor + 1, maior) if i % 2 != 0)

    print(f"O maior número é {maior}.")
    print(f"A somatória dos números ímpares entre {menor} e {maior} é {soma_impares}.")

main()