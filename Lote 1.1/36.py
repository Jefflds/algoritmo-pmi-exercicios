# Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

while True:
    try:
        numero_str = input("Informe um número N (ou 'S' para sair): ").strip()
        if numero_str.upper() == 'S':
            break
        n = int(numero_str)
    except ValueError:
        print("Entrada inválida. Informe um número inteiro.")
        continue

    if n < 0:
        print("O número deve ser não-negativo.")
        continue

    # Calcular a série
    soma = 1  # Primeiro termo é 1
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
        soma += 1 / fatorial

    print(f"A série 1 + 1/1! + 1/2! + ... + 1/{n}! = {soma:.6f}")
    
    continue_input = input("Deseja calcular outra série? (S/N): ")
    if continue_input.upper() == 'N':
        break