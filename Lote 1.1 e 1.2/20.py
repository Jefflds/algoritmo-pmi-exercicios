import cmath

# Receba 3 coeficientes A, B e C de uma equação do 2º grau da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.
# igual exercicio 5.
coefficientA: float = 0.0
coefficientB: float = 0.0
coefficientC: float = 0.0
delta: float = 0.0
x1: float = 0.0
x2: float = 0.0

def sanitize_input(user_input: str) -> float:
    user_input = user_input.replace(',', '.').replace(' ', '').strip()
    try:
        value = float(user_input)
        return value
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return 0.0

def calc_delta(a: float, b: float, c: float) -> float:
    return (b * b) - (4 * a * c)

def calc_roots(a: float, b: float, delta: float) -> tuple[float, float]:
    if delta < 0:
        return (0.0, 0.0)
    if a == 0:
        raise ValueError("Coeficiente 'a' não pode ser zero em uma função quadrática.")
    sqrt_delta = cmath.sqrt(delta)

    x1 = (-b + sqrt_delta) / (2 * a)
    x2 = (-b - sqrt_delta) / (2 * a)
    return (x1, x2)

def main() -> None:
    while True:
        userAInput = input("Digite o coeficiente A (ou 'S' para sair): ")
        if userAInput.upper() == 'S':
            break

        coefficientA = sanitize_input(userAInput)
        if coefficientA == 0:
            print("Coeficiente 'a' não pode ser zero em uma função quadrática.")
            continue

        userBInput = input("Digite o coeficiente B: ")
        coefficientB = sanitize_input(userBInput)

        userCInput = input("Digite o coeficiente C: ")
        coefficientC = sanitize_input(userCInput)

        delta = calc_delta(coefficientA, coefficientB, coefficientC)

        if delta < 0:
            print("A equação não possui raízes reais.")
        else:
            x1, x2 = calc_roots(coefficientA, coefficientB, delta)
            print(f"As raízes reais são: x1 = {x1.real:.2f}, x2 = {x2.real:.2f}")

main()