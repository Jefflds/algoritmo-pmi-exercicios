# Coletar o valor do lado de um quadrado, calcular sua área e apresentar o resultado. 
side: float = 0.0
area: float = 0.0

def calc_area(side: float) -> float:
    return side * side

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
        userSideInput = input("Digite o valor do lado do quadrado (ou 'S' para sair): ")
        if userSideInput.upper() == 'S':
            break
        side = sanitize_input(userSideInput)
        area = calc_area(side)
        print(f"A área do quadrado é: {area}")

main()