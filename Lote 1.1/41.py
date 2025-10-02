# Mostre todas as possibilidades de 2 dados de forma que a soma seja 7.

print("Todas as possibilidades de 2 dados cuja soma seja 7:")
print("Dado 1\tDado 2\tSoma")

for dado1 in range(1, 7):  # Valores de 1 a 6
    for dado2 in range(1, 7):  # Valores de 1 a 6
        if dado1 + dado2 == 7:
            print(f"{dado1}\t{dado2}\t{dado1 + dado2}")

input("Pressione Enter para sair...")