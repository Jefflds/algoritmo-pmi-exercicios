# Receba o número da base e do expoente. Calcule e mostre o valor da potência.

while True:
    try:
        base_str = input("Informe a base (ou 'S' para sair): ").strip()
        if base_str.upper() == 'S':
            break
        base = float(base_str)
        expoente_str = input("Informe o expoente: ").strip()
        expoente = float(expoente_str)
    except ValueError:
        print("Entrada inválida. Informe números válidos.")
        continue

    # Calcular potência
    resultado = base ** expoente
    print(f"{base} elevado a {expoente} = {resultado}")
    
    continue_input = input("Deseja calcular outra potência? (S/N): ")
    if continue_input.upper() == 'N':
        break