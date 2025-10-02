# Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N'nésimo termo.

while True:
    try:
        numero_str = input("Informe um número inteiro N (ou 'S' para sair): ").strip()
        if numero_str.upper() == 'S':
            break
        n = int(numero_str)
    except ValueError:
        print("Entrada inválida. Informe um número inteiro.")
        continue

    if n <= 0:
        print("O número deve ser positivo.")
        continue

    # Calcular e mostrar série de Fibonacci
    print(f"Série de Fibonacci até o {n}º termo:")
    if n >= 1:
        a, b = 0, 1
        print(f"1º termo: {a}")
        if n >= 2:
            print(f"2º termo: {b}")
            for i in range(3, n + 1):
                c = a + b
                print(f"{i}º termo: {c}")
                a, b = b, c
    
    continue_input = input("Deseja calcular outra série de Fibonacci? (S/N): ")
    if continue_input.upper() == 'N':
        break