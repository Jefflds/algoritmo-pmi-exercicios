# Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em fahrenheit F = (9*C+160) /5
celsius: float = 0.0
fahrenheit: float = 0.0

def calc_fahrenheit(celsius: float) -> float:
    return (9 * celsius + 160) / 5

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
        userCelsiusInput = input("Digite a temperatura em graus Celsius (ou 'S' para sair): ")
        if userCelsiusInput.upper() == 'S':
            break
        celsius = sanitize_input(userCelsiusInput)
        fahrenheit = calc_fahrenheit(celsius)
        print(f"A temperatura em graus Fahrenheit é: {fahrenheit}")

main()