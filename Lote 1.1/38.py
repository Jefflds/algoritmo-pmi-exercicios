# Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.

print("Digite 100 números positivos:")
maior = 0
menor = float('inf')
count = 0

while count < 100:
    try:
        numero_str = input(f"Digite o {count + 1}º número (ou 'S' para sair): ").strip()
        if numero_str.upper() == 'S':
            print(f"Encerrando com {count} números inseridos.")
            break
        numero = float(numero_str)
    except ValueError:
        print("Entrada inválida. Digite um número.")
        continue

    if numero <= 0:
        print("Somente valores positivos são aceitos.")
        continue

    # Atualizar maior e menor
    if count == 0:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    
    count += 1

if count > 0:
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
else:
    print("Nenhum número válido foi inserido.")