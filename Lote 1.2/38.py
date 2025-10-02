# Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.

def main():
    numeros = []
    for _ in range(100):
        while True:
            try:
                num = float(input("Informe um número real (positivo): "))
                if num < 0:
                    print("Por favor, informe um número positivo.")
                else:
                    numeros.append(num)
                    break
            except ValueError:
                print("Entrada inválida. Informe um número real.")

    if numeros:
        maior = max(numeros)
        menor = min(numeros)
        print(f"O maior valor informado é: {maior}")
        print(f"O menor valor informado é: {menor}")
    else:
        print("Nenhum número válido foi informado.")

main()