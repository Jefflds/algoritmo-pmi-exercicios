# Receba 2 números inteiros e mostre todos os números primos entre eles.

while True:
    try:
        num1_str = input("Informe o primeiro número inteiro (ou 'S' para sair): ").strip()
        if num1_str.upper() == 'S':
            break
        num1 = int(num1_str)
        num2_str = input("Informe o segundo número inteiro: ").strip()
        num2 = int(num2_str)
    except ValueError:
        print("Entrada inválida. Informe números inteiros.")
        continue

    # Determinar o intervalo
    inicio = min(num1, num2)
    fim = max(num1, num2)

    print(f"Números primos entre {inicio} e {fim}:")
    primos_encontrados = []

    for numero in range(max(2, inicio), fim + 1):
        # Verificar se é primo
        eh_primo = True
        if numero < 2:
            eh_primo = False
        else:
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    eh_primo = False
                    break
        
        if eh_primo:
            primos_encontrados.append(numero)

    if primos_encontrados:
        print(", ".join(map(str, primos_encontrados)))
    else:
        print("Nenhum número primo encontrado no intervalo.")
    
    continue_input = input("Deseja verificar outro intervalo? (S/N): ")
    if continue_input.upper() == 'N':
        break