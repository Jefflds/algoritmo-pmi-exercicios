# Coletar o valor do lado de um quadrado, calcular sua área e apresentar o resultado.

while True:
    userSideInput = input("Digite o valor do lado do quadrado (ou 'S' para sair): ")
    if userSideInput.upper() == 'S':
        break
    
    # Sanitizar entrada
    userSideInput = userSideInput.replace(',', '.').replace(' ', '').strip()
    try:
        side = float(userSideInput)
        # Calcular área
        area = side * side
        print(f"A área do quadrado é: {area}")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
