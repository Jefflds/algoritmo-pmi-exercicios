# Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

def main():
    try:
        valor1_str = input("Informe o primeiro valor inteiro: ").strip()
        valor1 = int(valor1_str)
        valor2_str = input("Informe o segundo valor inteiro: ").strip()
        valor2 = int(valor2_str)
    except Exception:
        print("Entrada inválida. Informe números inteiros.")
        return

    if valor1 > valor2:
        diferenca = valor1 - valor2
    else:
        diferenca = valor2 - valor1

    print(f"A diferença do maior pelo menor valor é: {diferenca}")

main()