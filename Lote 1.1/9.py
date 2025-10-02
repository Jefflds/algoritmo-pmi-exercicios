# Receba os 2 números inteiros. Calcule e mostre a soma dos quadrados.

while True:
    try:
        first_number = int(input("Digite o primeiro número inteiro (ou 'S' para sair): ").strip())
    except ValueError as e:
        if str(e).find("S") != -1 or str(e).find("s") != -1:
            break
        print("Entrada inválida. Por favor, insira um número inteiro.")
        continue
    
    try:
        second_number = int(input("Digite o segundo número inteiro: ").strip())
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
        continue

    # Calcular soma dos quadrados
    sum_of_squares = first_number**2 + second_number**2
    print(f"A soma dos quadrados de {first_number} e {second_number} é: {sum_of_squares}")
    
    continue_input = input("Deseja calcular novamente? (S/N): ")
    if continue_input.upper() == 'N':
        break