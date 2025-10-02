# Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.

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

    # Determinar menor e maior
    if num1 > num2:
        maior, menor = num1, num2
    else:
        maior, menor = num2, num1

    # Calcular soma dos números ímpares no intervalo
    soma_impares = 0
    for i in range(menor + 1, maior):
        if i % 2 != 0:  # Número ímpar
            soma_impares += i

    print(f"A somatória dos números ímpares entre {menor} e {maior} é: {soma_impares}")
    
    continue_input = input("Deseja calcular outra somatória? (S/N): ")
    if continue_input.upper() == 'N':
        break