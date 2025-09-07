# Receba um número. Calcule e mostre os resultados da tabuada desse número.
def main():
    try:
        n = int(input("Informe um número inteiro: "))
    except ValueError:
        print("Entrada inválida. Informe um número inteiro.")
        return

    print(f"Tabuada de {n}:")
    for i in range(1, 11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")

main()