# Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.

while True:
    try:
        cateto1_str = input("Informe o valor do 1º cateto (ou 'S' para sair): ").strip()
        if cateto1_str.upper() == 'S':
            break
        cateto2_str = input("Informe o valor do 2º cateto: ").strip()
        cateto1 = float(cateto1_str)
        cateto2 = float(cateto2_str)
    except ValueError:
        print("Entrada inválida. Informe números válidos para os catetos.")
        continue

    if cateto1 <= 0 or cateto2 <= 0:
        print("Os catetos devem ser positivos.")
        continue

    # Calcular hipotenusa usando teorema de Pitágoras
    hipotenusa = (cateto1**2 + cateto2**2) ** 0.5

    print(f"A hipotenusa é: {hipotenusa}")
    
    continue_input = input("Deseja calcular outra hipotenusa? (S/N): ")
    if continue_input.upper() == 'N':
        break