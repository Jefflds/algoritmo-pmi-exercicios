# Receba um número inteiro. Calcule e mostre o seu fatorial.

while True:
    try:
        numero_str = input("Informe um número inteiro (ou 'S' para sair): ").strip()
        if numero_str.upper() == 'S':
            break
        numero = int(numero_str)
    except ValueError:
        print("Entrada inválida. Informe um número inteiro.")
        continue

    if numero < 0:
        print("Fatorial não é definido para números negativos.")
        continue

    # Calcular fatorial
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i

    print(f"O fatorial de {numero} é {fatorial}")
    
    continue_input = input("Deseja calcular outro fatorial? (S/N): ")
    if continue_input.upper() == 'N':
        break