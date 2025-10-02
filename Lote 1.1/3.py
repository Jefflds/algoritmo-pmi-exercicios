# Receba a base e a altura de um triângulo. Calcule e mostre a sua área.

while True:
    userBaseInput = input("Digite a base do triângulo: ")
    userBaseInput = userBaseInput.replace(',', '.').replace(' ', '').strip()
    try:
        base = float(userBaseInput)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        continue

    userHeightInput = input("Digite a altura do triângulo: ")
    userHeightInput = userHeightInput.replace(',', '.').replace(' ', '').strip()
    try:
        height = float(userHeightInput)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        continue

    # Calcular área
    area = (base * height) / 2
    print(f"A área do triângulo é: {area}")

    continueInput = input("Deseja calcular a área de outro triângulo? (S/N): ")
    if continueInput.upper() == 'N':
        break