# Receba o número da base e do expoente. Calcule e mostre o valor da potência.

def power(base, exponent):
    return base ** exponent

def main():
    base = float(input("Digite a base (número real): "))
    exponent = float(input("Digite o expoente (número real): "))
    result = power(base, exponent)
    print(f"{base} elevado a {exponent} é igual a {result}")

main()