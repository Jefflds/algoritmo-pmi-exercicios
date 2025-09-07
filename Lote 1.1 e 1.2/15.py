# Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.

def main():
    try:
        cateto1_str = input("Informe o valor do 1º cateto: ").strip()
        cateto2_str = input("Informe o valor do 2º cateto: ").strip()
        cateto1 = float(cateto1_str)
        cateto2 = float(cateto2_str)
    except Exception:
        print("Entrada inválida. Informe números válidos para os catetos.")
        return

    if cateto1 <= 0 or cateto2 <= 0:
        print("Os catetos devem ser positivos.")
        return

    hipotenusa = (cateto1**2 + cateto2**2) ** 0.5

    print(f"A hipotenusa é: {hipotenusa}")

main()