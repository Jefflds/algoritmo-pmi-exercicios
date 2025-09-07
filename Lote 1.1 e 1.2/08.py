#Receba o valor de um depósito em poupança. Calcule e mostre o valor e após 1 mês de aplicação sabendo que rende 1,3% a. m.
def sanitize_input(user_input: str) -> float:
    user_input = user_input.replace(',', '.').replace(' ', '').strip()
    try:
        value = float(user_input)
        return value
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return 0.0

def main() -> None:
    rate: float = 1.3 / 100
    months: int = 1

    while True:
        userAmountInput = input("Digite o valor do depósito (ou 'S' para sair): ")
        if userAmountInput.upper() == 'S':
            break

        userPercentageInput = input("Digite a taxa de juros (padrão é 1,3%): ")
        if userPercentageInput.strip() != '':
            rate = sanitize_input(userPercentageInput) / 100

        userMonthsInput = input("Digite o número de meses (padrão é 1): ")
        if userMonthsInput.strip() != '':
            months = int(userMonthsInput)

        amount = sanitize_input(userAmountInput)
        amount_after_n_months = amount * (1 + rate) ** months

        print(f"Após {months} meses, o valor do depósito será: {amount_after_n_months:.2f}")

main()