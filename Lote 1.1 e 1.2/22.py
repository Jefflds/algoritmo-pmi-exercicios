# Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.

def main():
    try:
        v1_str = input("Informe o primeiro valor inteiro: ").strip()
        v1 = int(v1_str)
        v2_str = input("Informe o segundo valor inteiro (diferente do primeiro): ").strip()
        v2 = int(v2_str)
        if v1 == v2:
            print("Os valores devem ser diferentes.")
            return
    except ValueError:
        print("Entrada inválida. Informe números inteiros válidos.")
        return

    if v1 < v2:
        menor, maior = v1, v2
    else:
        menor, maior = v2, v1

    print(f"Valores em ordem crescente: {menor}, {maior}")

main()