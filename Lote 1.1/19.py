# Receba 2 valores reais. Calcule e mostre o maior deles.

while True:
    try:
        v1_str = input("Informe o primeiro valor (ou 'S' para sair): ").strip()
        if v1_str.upper() == 'S':
            break
        v1 = float(v1_str.replace(',', '.'))
        v2_str = input("Informe o segundo valor: ").strip()
        v2 = float(v2_str.replace(',', '.'))
    except ValueError:
        print("Entrada inválida. Informe números válidos.")
        continue

    # Encontrar o maior valor
    if v1 > v2:
        maior = v1
    else:
        maior = v2

    print(f"O maior valor é: {maior:.2f}")
    
    continue_input = input("Deseja comparar outros valores? (S/N): ")
    if continue_input.upper() == 'N':
        break