# Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume.
length: float = 0.0
width: float = 0.0
height: float = 0.0
volume: float = 0.0

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
        userLengthInput = input("Digite o comprimento (ou 'S' para sair): ")
        if userLengthInput.upper() == 'S':
            break

        userWidthInput = input("Digite a largura: ")
        userHeightInput = input("Digite a altura: ")

        length = sanitize_input(userLengthInput)
        width = sanitize_input(userWidthInput)
        height = sanitize_input(userHeightInput)

        volume = length * width * height

        volume = float(userLengthInput) * float(userWidthInput) * float(userHeightInput)
        print("O volume do paralelepípedo é:", volume)

main()