# Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

def main():
    try:
        valor_str = input("Informe um valor inteiro: ").strip()
        valor = int(valor_str)
    except ValueError:
        print("Entrada inválida. Informe um número inteiro válido.")
        return

    divisivel_por_2 = (valor % 2 == 0)
    divisivel_por_3 = (valor % 3 == 0)

    if divisivel_por_2 and divisivel_por_3:
        print(f"O valor {valor} é divisível por 2 e por 3.")
    elif divisivel_por_2:
        print(f"O valor {valor} é divisível por 2, mas não por 3.")
    elif divisivel_por_3:
        print(f"O valor {valor} é divisível por 3, mas não por 2.")
    else:
        print(f"O valor {valor} não é divisível nem por 2 nem por 3.")
        
main()