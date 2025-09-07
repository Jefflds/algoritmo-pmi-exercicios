# Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.

def main():
    try:
        num1_str = input("Informe o primeiro número inteiro: ").strip()
        num2_str = input("Informe o segundo número inteiro: ").strip()
        num1 = int(num1_str)
        num2 = int(num2_str)
    except ValueError:
        print("Entrada inválida. Informe números inteiros válidos.")
        return

    if num1 == 0 or num2 == 0:
        print("Nenhum número pode ser zero.")
        return

    maior = max(num1, num2)
    menor = min(num1, num2)

    if maior % menor == 0:
        print(f"{maior} é múltiplo de {menor}.")
    else:
        print(f"{maior} não é múltiplo de {menor}.")
main()