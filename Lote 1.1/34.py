# Receba um número. Calcule e mostre os resultados da tabuada desse número.

while True:
    try:
        numero_str = input("Informe um número para a tabuada (ou 'S' para sair): ").strip()
        if numero_str.upper() == 'S':
            break
        numero = float(numero_str)
    except ValueError:
        print("Entrada inválida. Informe um número.")
        continue

    # Mostrar tabuada
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    
    continue_input = input("Deseja ver outra tabuada? (S/N): ")
    if continue_input.upper() == 'N':
        break