#  Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
# Casa: 1 2 3 4 ... 64
# Qdte: 1 2 4 8 ... N

def main():
    try:
        n = int(input("Informe o número de casas do tabuleiro (1 a 64): "))
        if n < 1 or n > 64:
            print("Por favor, informe um número entre 1 e 64.")
            return
    except ValueError:
        print("Entrada inválida. Informe um número inteiro.")
        return

    graos = 2**(n - 1)

    print(f"A quantidade de grãos na casa {n} é {graos}.")
main()
