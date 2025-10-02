# Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais.
import cmath

while True:
    userAInput = input("Digite o coeficiente A (ou 'S' para sair): ")
    if userAInput.upper() == 'S':
        break

    # Sanitizar entrada A
    userAInput = userAInput.replace(',', '.').replace(' ', '').strip()
    try:
        coefficientA = float(userAInput)
        if coefficientA == 0:
            print("Coeficiente 'a' não pode ser zero em uma função quadrática.")
            continue
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        continue

    userBInput = input("Digite o coeficiente B: ")
    userBInput = userBInput.replace(',', '.').replace(' ', '').strip()
    try:
        coefficientB = float(userBInput)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        continue

    userCInput = input("Digite o coeficiente C: ")
    userCInput = userCInput.replace(',', '.').replace(' ', '').strip()
    try:
        coefficientC = float(userCInput)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        continue

    # Calcular delta
    delta = (coefficientB * coefficientB) - (4 * coefficientA * coefficientC)

    if delta < 0:
        print("A equação não possui raízes reais.")
    else:
        # Calcular raízes
        sqrt_delta = cmath.sqrt(delta)
        x1 = (-coefficientB + sqrt_delta) / (2 * coefficientA)
        x2 = (-coefficientB - sqrt_delta) / (2 * coefficientA)
        print(f"As raízes reais são: x1 = {x1.real:.2f}, x2 = {x2.real:.2f}")