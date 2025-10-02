# Receba 2 números reais. Calcule e mostre a diferença desses valores.

while True:
    userFirstValueInput = input("Digite o primeiro número real (ou 'S' para sair): ")
    if userFirstValueInput.upper() == 'S':
        break
    
    # Sanitizar primeira entrada
    userFirstValueInput = userFirstValueInput.replace(',', '.').replace(' ', '').strip()
    try:
        firstValue = float(userFirstValueInput)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        continue

    userSecondValueInput = input("Digite o segundo número real: ")
    # Sanitizar segunda entrada
    userSecondValueInput = userSecondValueInput.replace(',', '.').replace(' ', '').strip()
    try:
        secondValue = float(userSecondValueInput)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        continue

    # Calcular diferença
    difference = firstValue - secondValue
    print(f"A diferença entre {firstValue} e {secondValue} é: {difference}")