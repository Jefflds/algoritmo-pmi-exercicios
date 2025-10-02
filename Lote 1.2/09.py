# Receba os 2 números inteiros. Calcule e mostre a soma dos quadrados.
def main() -> None:
    first_number: int = int(input("Digite o primeiro número inteiro: ").strip())
    second_number: int = int(input("Digite o segundo número inteiro: ").strip())

    sum_of_squares: int = first_number**2 + second_number**2

    print(f"A soma dos quadrados de {first_number} e {second_number} é: {sum_of_squares}")

main() 