# Receba 2 valores reais. Calcule e mostre o maior deles.

def main():
    try:
        v1_str = input("Informe o primeiro valor: ").strip()
        v1 = float(v1_str.replace(',', '.'))
        v2_str = input("Informe o segundo valor: ").strip()
        v2 = float(v2_str.replace(',', '.'))
    except ValueError:
        print("Entrada inválida. Informe números válidos.")
        return

    if v1 > v2:
        maior = v1
    else:
        maior = v2

    print(f"O maior valor é: {maior:.2f}")

main()