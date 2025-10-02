# Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume.

while True:
    userLengthInput = input("Digite o comprimento (ou 'S' para sair): ")
    if userLengthInput.upper() == 'S':
        break

    userWidthInput = input("Digite a largura: ")
    userHeightInput = input("Digite a altura: ")

    # Sanitizar entradas
    userLengthInput = userLengthInput.replace(',', '.').replace(' ', '').strip()
    userWidthInput = userWidthInput.replace(',', '.').replace(' ', '').strip()
    userHeightInput = userHeightInput.replace(',', '.').replace(' ', '').strip()
    
    try:
        length = float(userLengthInput)
        width = float(userWidthInput)
        height = float(userHeightInput)
        
        # Calcular volume
        volume = length * width * height
        print("O volume do paralelepípedo é:", volume)
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")