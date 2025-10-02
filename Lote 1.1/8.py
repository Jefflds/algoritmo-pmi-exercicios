# Receba o valor de um depósito em poupança. Calcule e mostre o valor e após 1 mês de aplicação sabendo que rende 1,3% a. m.

while True:
    userAmountInput = input("Digite o valor do depósito (ou 'S' para sair): ")
    if userAmountInput.upper() == 'S':
        break

    rate = 1.3 / 100
    months = 1

    userPercentageInput = input("Digite a taxa de juros (padrão é 1,3%): ")
    if userPercentageInput.strip() != '':
        userPercentageInput = userPercentageInput.replace(',', '.').replace(' ', '').strip()
        try:
            rate = float(userPercentageInput) / 100
        except ValueError:
            print("Taxa inválida. Usando 1,3%.")
            rate = 1.3 / 100

    userMonthsInput = input("Digite o número de meses (padrão é 1): ")
    if userMonthsInput.strip() != '':
        try:
            months = int(userMonthsInput)
        except ValueError:
            print("Número de meses inválido. Usando 1.")
            months = 1

    # Sanitizar entrada do valor
    userAmountInput = userAmountInput.replace(',', '.').replace(' ', '').strip()
    try:
        amount = float(userAmountInput)
        # Calcular valor após aplicação
        amount_after_n_months = amount * (1 + rate) ** months
        print(f"Após {months} meses, o valor do depósito será: {amount_after_n_months:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")