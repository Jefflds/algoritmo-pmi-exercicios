# Receba um número inteiro. Calcule e mostre o seu fatorial.

def main():
    try:
        numero = int(input("Informe um número inteiro não negativo: "))
        if numero < 0:
            print("Número inválido. Informe um número inteiro não negativo.")
            return
    except ValueError:
        print("Entrada inválida. Informe um número inteiro.")
        return

    fatorial = 1
    for i in range(2, numero + 1):
        fatorial *= i

    print(f"O fatorial de {numero} é {fatorial}.")
main()