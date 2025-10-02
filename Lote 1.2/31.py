# Calcule e mostre o quadrado dos números entre 10 e 150.

def main():
    for numero in range(10, 151):
        quadrado = numero ** 2
        print(f"O quadrado de {numero} é {quadrado}")

main()