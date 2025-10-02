#Receba a base e a altura de um triângulo. Calcule e mostre a sua área.
base: float = 0.0
height: float = 0.0
area: float = 0.0

def calc_area(base: float, height: float) -> float:
    return (base * height) / 2

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
        userBaseInput = input("Digite a base do triângulo: ")
        base = sanitize_input(userBaseInput)

        userHeightInput = input("Digite a altura do triângulo: ")
        height = sanitize_input(userHeightInput)

        area = calc_area(base, height)
        print(f"A área do triângulo é: {area}")

        continueInput = input("Deseja calcular a área de outro triângulo? (S/N): ")
        if continueInput.upper() == 'N':
            break

main()