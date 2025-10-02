# Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados

def main():
    try:
        tipo_investimento = int(input("Informe o tipo de investimento (1 = poupança, 2 = renda fixa): ").strip())
        valor_investimento = float(input("Informe o valor do investimento: ").strip())
    except ValueError:
        print("Entrada inválida. Informe números inteiros para o tipo de investimento e números decimais para o valor.")
        return

    if tipo_investimento == 1:
        # Poupança
        rendimento = valor_investimento * 0.03
    elif tipo_investimento == 2:
        # Renda fixa
        rendimento = valor_investimento * 0.05
    else:
        print("Tipo de investimento não reconhecido.")
        return

    valor_corrigido = valor_investimento + rendimento
    print(f"Valor corrigido em 30 dias: {valor_corrigido:.2f}")

main()