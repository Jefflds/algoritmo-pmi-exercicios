# Receba 2 números reais. Calcule e mostre a diferença desses valores.
firstValue: float = 0.0
secondValue: float = 0.0
difference: float = 0.0

def sanitize_input(user_input: str) -> float:
    user_input = user_input.replace(',', '.').replace(' ', '').strip()
    try:
        value = float(user_input)
        return value
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return 0.0
    
def main() -> None:
    while True:
        userFirstValueInput = input("Digite o primeiro número real (ou 'S' para sair): ")
        if userFirstValueInput.upper() == 'S':
            break
        firstValue = sanitize_input(userFirstValueInput)

        userSecondValueInput = input("Digite o segundo número real (ou 'S' para sair): ")
        if userSecondValueInput.upper() == 'S':
            break
        secondValue = sanitize_input(userSecondValueInput)

        difference = firstValue - secondValue

        print(f"A diferença entre {firstValue} e {secondValue} é: {difference}")

main()