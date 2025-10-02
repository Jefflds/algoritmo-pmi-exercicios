# Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225

print("Calculando a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225:")
soma = 0

for i in range(1, 16):  # i de 1 a 15
    denominador = i * i  # i²
    termo = i / denominador
    
    # Alternar sinal: positivo para ímpares, negativo para pares
    if i % 2 == 0:
        termo = -termo
    
    soma += termo
    sinal = "+" if termo > 0 else ""
    print(f"Termo {i}: {sinal}{termo:.6f} (= {sinal}{i}/{denominador})")

print(f"\nSoma da série: {soma:.6f}")
input("Pressione Enter para sair...")