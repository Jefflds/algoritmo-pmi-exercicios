# Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados

while True:
    try:
        tipo_str = input("Informe o tipo de investimento (1 = poupança, 2 = renda fixa) ou 'S' para sair: ").strip()
        if tipo_str.upper() == 'S':
            break
        tipo_investimento = int(tipo_str)
        valor_investimento = float(input("Informe o valor do investimento: ").strip())
    except ValueError:
        print("Entrada inválida. Informe números inteiros para o tipo de investimento e números decimais para o valor.")
        continue

    # Calcular rendimento baseado no tipo
    if tipo_investimento == 1:
        # Poupança
        rendimento = valor_investimento * 0.03
        tipo_nome = "poupança"
    elif tipo_investimento == 2:
        # Renda fixa
        rendimento = valor_investimento * 0.05
        tipo_nome = "renda fixa"
    else:
        print("Tipo de investimento não reconhecido.")
        continue

    valor_corrigido = valor_investimento + rendimento
    print(f"Valor corrigido em 30 dias ({tipo_nome}): {valor_corrigido:.2f}")
    
    continue_input = input("Deseja calcular outro investimento? (S/N): ")
    if continue_input.upper() == 'N':
        break