# Receba o raio de uma circunferência. Calcule e mostre o comprimento da circunferência.
# C = 2 * π * r (C = comprimento, r = raio, π = 3.14)

while True:
    try:
        raio_str = input("Informe o raio da circunferência (ou 'S' para sair): ").strip()
        if raio_str.upper() == 'S':
            break
        raio = float(raio_str)
    except ValueError:
        print("Entrada inválida. Informe um número para o raio.")
        continue

    pi = 3.14
    # Calcular comprimento da circunferência
    comprimento = 2 * pi * raio
    print(f"Comprimento da circunferência: {comprimento:.2f}")
    
    continue_input = input("Deseja calcular outro comprimento? (S/N): ")
    if continue_input.upper() == 'N':
        break