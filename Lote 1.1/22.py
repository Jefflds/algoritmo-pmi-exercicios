# Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.

while True:
    try:
        v1_str = input("Informe o primeiro valor inteiro (ou 'S' para sair): ").strip()
        if v1_str.upper() == 'S':
            break
        v1 = int(v1_str)
        v2_str = input("Informe o segundo valor inteiro (diferente do primeiro): ").strip()
        v2 = int(v2_str)
        if v1 == v2:
            print("Os valores devem ser diferentes.")
            continue
    except ValueError:
        print("Entrada inválida. Informe números inteiros válidos.")
        continue

    # Ordenar em ordem crescente
    if v1 < v2:
        menor, maior = v1, v2
    else:
        menor, maior = v2, v1

    print(f"Valores em ordem crescente: {menor}, {maior}")
    
    continue_input = input("Deseja ordenar outros valores? (S/N): ")
    if continue_input.upper() == 'N':
        break