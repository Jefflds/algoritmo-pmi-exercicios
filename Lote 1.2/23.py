# Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.
def main():
    try:
        v1_str = input("Informe o primeiro valor (menor): ").strip()
        v1 = float(v1_str)
        v2_str = input("Informe o segundo valor (médio): ").strip()
        v2 = float(v2_str)
        v3_str = input("Informe o terceiro valor (maior): ").strip()
        v3 = float(v3_str)
        v4_str = input("Informe o quarto valor (não necessariamente em ordem): ").strip()
        v4 = float(v4_str)
    except ValueError:
        print("Entrada inválida. Informe números válidos.")
        return

    if v1 > v2 or v2 > v3:
        print("Os três primeiros valores devem estar em ordem crescente.")
        return

    valores = [v1, v2, v3, v4]
    valores.sort()
    print("Valores em ordem crescente:", valores)

main()