# Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

while True:
    try:
        valor_str = input("Informe um valor inteiro (ou 'S' para sair): ").strip()
        if valor_str.upper() == 'S':
            break
        valor = int(valor_str)
    except ValueError:
        print("Entrada inválida. Informe um número inteiro válido.")
        continue

    # Verificar divisibilidade
    divisivel_por_2 = (valor % 2 == 0)
    divisivel_por_3 = (valor % 3 == 0)

    if divisivel_por_2 and divisivel_por_3:
        print(f"O valor {valor} é divisível por 2 e por 3.")
    elif divisivel_por_2:
        print(f"O valor {valor} é divisível por 2, mas não por 3.")
    elif divisivel_por_3:
        print(f"O valor {valor} é divisível por 3, mas não por 2.")
    else:
        print(f"O valor {valor} não é divisível nem por 2 nem por 3.")
        
    continue_input = input("Deseja verificar outro valor? (S/N): ")
    if continue_input.upper() == 'N':
        break