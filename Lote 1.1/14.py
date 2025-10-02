# Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo.

while True:
    try:
        angulo1_str = input("Informe o 1º ângulo (ou 'S' para sair): ").strip()
        if angulo1_str.upper() == 'S':
            break
        angulo2_str = input("Informe o 2º ângulo: ").strip()
        angulo1 = float(angulo1_str)
        angulo2 = float(angulo2_str)
    except ValueError:
        print("Entrada inválida. Informe números válidos para os ângulos.")
        continue

    if angulo1 <= 0 or angulo2 <= 0:
        print("Os ângulos devem ser positivos.")
        continue

    # Calcular terceiro ângulo
    angulo3 = 180 - (angulo1 + angulo2)

    if angulo3 <= 0:
        print("A soma dos ângulos deve ser igual a 180 graus.")
        continue

    print(f"O 3º ângulo é: {angulo3} graus.")
    
    continue_input = input("Deseja calcular outro triângulo? (S/N): ")
    if continue_input.upper() == 'N':
        break