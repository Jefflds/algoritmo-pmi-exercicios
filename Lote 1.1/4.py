# Receba a temperatura em graus Celsius. Calcule e mostre a sua temperatura convertida em fahrenheit F = (9*C+160) /5

while True:
    userCelsiusInput = input("Digite a temperatura em graus Celsius (ou 'S' para sair): ")
    if userCelsiusInput.upper() == 'S':
        break
    
    # Sanitizar entrada
    userCelsiusInput = userCelsiusInput.replace(',', '.').replace(' ', '').strip()
    try:
        celsius = float(userCelsiusInput)
        # Calcular fahrenheit
        fahrenheit = (9 * celsius + 160) / 5
        print(f"A temperatura em graus Fahrenheit é: {fahrenheit}")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")