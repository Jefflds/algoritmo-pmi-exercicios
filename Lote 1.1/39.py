# Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
# Casa: 1 2 3 4 ... 64
# Qdte: 1 2 4 8 ... N

print("Calculando grãos no tabuleiro de xadrez:")
print("Casa\tGrãos")
total_graos = 0

for casa in range(1, 65):
    graos_casa = 2 ** (casa - 1)  # 2^(n-1) onde n é o número da casa
    total_graos += graos_casa
    print(f"{casa}\t{graos_casa}")

print(f"\nTotal de grãos no tabuleiro: {total_graos}")
input("Pressione Enter para sair...")