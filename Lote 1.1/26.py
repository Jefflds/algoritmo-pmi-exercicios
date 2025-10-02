# Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.

while True:
    try:
        num1_str = input("Informe o primeiro número inteiro (ou 'S' para sair): ").strip()
        if num1_str.upper() == 'S':
            break
        num1 = int(num1_str)
        num2_str = input("Informe o segundo número inteiro: ").strip()
        num2 = int(num2_str)
    except ValueError:
        print("Entrada inválida. Informe números inteiros válidos.")
        continue

    if num1 == 0 or num2 == 0:
        print("Os números devem ser diferentes de zero.")
        continue

    # Determinar maior e menor
    if num1 > num2:
        maior, menor = num1, num2
    else:
        maior, menor = num2, num1

    # Verificar se maior é múltiplo do menor
    if maior % menor == 0:
        print(f"{maior} é múltiplo de {menor}.")
    else:
        print(f"{maior} não é múltiplo de {menor}.")
        
    continue_input = input("Deseja verificar outros números? (S/N): ")
    if continue_input.upper() == 'N':
        break