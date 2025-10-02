# Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99

print("Calculando a série 1 + 2/3 + 3/5 + ... + 50/99:")
soma = 0

for i in range(1, 51):  # i de 1 a 50
    denominador = 2 * i - 1  # 1, 3, 5, 7, ..., 99
    termo = i / denominador
    soma += termo
    print(f"Termo {i}: {i}/{denominador} = {termo:.6f}")

print(f"\nSoma da série: {soma:.6f}")
input("Pressione Enter para sair...")