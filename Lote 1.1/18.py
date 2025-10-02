# Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

while True:
    try:
        valor1_str = input("Informe o primeiro valor inteiro (ou 'S' para sair): ").strip()
        if valor1_str.upper() == 'S':
            break
        valor1 = int(valor1_str)
        valor2_str = input("Informe o segundo valor inteiro: ").strip()
        valor2 = int(valor2_str)
    except ValueError:
        print("Entrada inválida. Informe números inteiros.")
        continue

    # Calcular diferença do maior pelo menor
    if valor1 > valor2:
        diferenca = valor1 - valor2
    else:
        diferenca = valor2 - valor1

    print(f"A diferença do maior pelo menor valor é: {diferenca}")
    
    continue_input = input("Deseja calcular outra diferença? (S/N): ")
    if continue_input.upper() == 'N':
        break